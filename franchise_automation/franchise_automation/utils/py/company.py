import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def company_customisation():
    company_property_setter()
    company_custom_fields()

def company_property_setter():
    pass

    
def company_custom_fields():
    custom_fields = {
        "Company": [
            dict(fieldname='franchise_automation', label='Franchise Automation',
                fieldtype='Tab Break',insert_after='registration_details',depends_on='eval:!doc.__islocal && doc.parent_company'),
            dict(fieldname='create_customer_supplier', label='➛ Create Customer',
                fieldtype='Button',insert_after='franchise_automation'),
            dict(fieldname='update_item_tax_table', label='➛ Update Item Tax Table',
                fieldtype='Button',insert_after='create_customer_supplier',hidden=1),
            dict(fieldname='update_mode_of_payment', label='➛ Update Mode of Payment',
                fieldtype='Button',insert_after='update_item_tax_table'),
            dict(fieldname='mode_of_payment', label='Mode of Payment',
                fieldtype='Table',insert_after='update_mode_of_payment',options='Company Mode of Payment'),
            dict(fieldname='pos_user', label='POS User',
                fieldtype='Check',insert_after='mode_of_payment'),
            dict(fieldname='create_pos', label='➛ Create POS',
                fieldtype='Button',insert_after='pos_user',depends_on='eval:doc.pos_user'),
            dict(fieldname='create_users', label='➛ Create Users',
                fieldtype='Button',insert_after='create_pos'),
            dict(fieldname='user_table', label='User Table',
                fieldtype='Table',options='Company Users',insert_after='create_user'),
            ],
            
    }
    create_custom_fields(custom_fields)

def validate_parent(doc):
    if doc.company_type == 'Parent':
        parent = frappe.get_all('Company',{'company_type':'Parent'})
        if len(parent) > 1:
            frappe.throw('Only one parent company should be created')

def create_supp_cust(doc,event):
    if doc.is_group and not doc.get('__islocal'):
        if not frappe.db.exists('Supplier Group','Parent Supplier'):
            new = frappe.new_doc('Supplier Group')
            new.supplier_group_name = 'Parent Supplier'
            new.save()

        if not frappe.db.exists('Supplier',doc.name):
            new_sup = frappe.new_doc('Supplier')
            new_sup.supplier_name = doc.name
            new_sup.supplier_group = 'Parent Supplier'
            new_sup.supplier_type = 'Company'
            new_sup.is_internal_supplier = 1
            new_sup.represents_company = doc.name
            new_sup.save()

    elif doc.parent_company and not doc.get('__islocal'):
        parent = frappe.get_value('Company',{'company_type':'Parent','name':doc.parent_company},'name')
        if frappe.db.exists('Supplier',parent):
            supp = frappe.get_doc('Supplier',parent)
            if not (frappe.db.exists('Allowed To Transact With',{'company':doc.name,'parent':supp.name})):
                supp.append('companies',{
                    'company':doc.name
                })
                supp.save()

@frappe.whitelist()
def create_pos(doc):
    doc = frappe.get_doc('Company',doc)
    if not frappe.db.exists('POS Profile',doc.name):
        pos = frappe.new_doc('POS Profile')
        pos.company = doc.name
        pos.__newname = doc.name
        pos.write_off_cost_center = f'Main - {doc.abbr}'
        pos.write_off_account = doc.write_off_account
        pos.warehouse = f'Stores - {doc.abbr}'
        pos.cost_center =  doc.cost_center
        pos.apply_discount_on = 'Net Total'
        pos.posa_display_items_in_stock =  1
        pos.posa_allow_return =  1
        pos.posa_auto_set_batch =  1
        pos.posa_display_additional_notes =  1
        pos.posa_display_items_in_stock =  1
        pos.posa_allow_duplicate_customer_names =  1
        pos.posa_search_serial_no = 1
        pos.posa_tax_inclusive = 1
        pos.posa_local_storage = 1
        pos.tax_category = 'In-State'
        pos.print_format = frappe.db.get_value(
                "Property Setter",
                dict(property="default_print_format", doc_type='POS Invoice'),
                "value",
            )
        for i in frappe.get_list('Item Group',{'show_franchise':1},pluck='name'):
            pos.append('item_groups',{
                'item_group':i,
            })
        pos.append('payments',{
            'mode_of_payment':"Cash",
            'default':1
        })
        pos.flags.ignore_mandatory = True
        pos.save()
        return 1
    else:
        return 0

@frappe.whitelist()
def create_mode(doc):
    doc = frappe.get_doc('Company',doc)
    # validate_parent(doc)
    if doc.parent_company:
        list_doc = frappe.get_all("Mode of Payment Account",{'company':doc.name},pluck='name')
        for j in list_doc:
            frappe.delete_doc('Mode of Payment Account',j)
            frappe.db.commit()
        for i in doc.mode_of_payment:
            if i.account and i.mode_of_payment and not frappe.db.exists('Mode of Payment Account',{'parent':i.mode_of_payment,'company':doc.name,'default_account':i.account}):
                
                child = frappe.get_doc('Mode of Payment',i.mode_of_payment)
                child.append('accounts',{
                    'company':doc.name,
                    'default_account':i.account
                })
                child.flags.ignore_validate = True
                child.save()
    return 1

@frappe.whitelist()
def update_item_tax_table(doc):
    doc = frappe.get_doc('Company',doc)
    hsn_list = frappe.get_all("GST HSN Code",pluck='name')
    for hs in hsn_list:
        hs_doc = frappe.get_doc('GST HSN Code',hs)
        if hs_doc.custom_tax_percentage:
            tax_template = f'GST {int(hs_doc.custom_tax_percentage)}% - {doc.abbr}'
            item_list = frappe.get_all('Item',{'gst_hsn_code':hs},pluck='name')
            for item in item_list:
                item_doc = frappe.get_doc('Item',item)  
                if not (frappe.db.exists('Item Tax',{'item_tax_template':tax_template,'tax_category':'In-State','parent':item_doc.name})):
                    item_doc.append('taxes',{
                        'item_tax_template':tax_template,
                        'tax_category':'In-State'
                    })
                if not (frappe.db.exists('Item Tax',{'item_tax_template':tax_template,'tax_category':'Out-State','parent':item_doc.name})):
                    item_doc.append('taxes',{
                        'item_tax_template':tax_template,
                        'tax_category':'Out-State'
                    })
                item_doc.save()
    
    return 1

@frappe.whitelist()
def update_supplier(doc):

    doc = frappe.get_doc('Company',doc)
    if not frappe.db.exists('Customer Group','Franchise Customer'):
        new = frappe.new_doc('Customer Group')
        new.customer_group_name = 'Franchise Customer'
        new.save()

    # Create Customer
    if not frappe.db.exists('Customer',{'customer_name':doc.name}):
        new_cus = frappe.new_doc('Customer')
        new_cus.company_type = 'Company'
        new_cus.customer_group = 'Franchise Customer'
        new_cus.customer_name = doc.name
        new_cus.is_internal_customer = 1
        new_cus.represents_company = doc.name
        new_cus.gstin = doc.gstin
        new_cus.gst_category = "Registered Regular" if doc.gstin else "Unregistered"
        new_cus.append('companies',{
            'company':doc.parent_company
        })
        new_cus.save()
        address=frappe.get_all(
            "Address",
            filters=[
            ["Dynamic Link", "link_doctype", "=", 'Company'],
            ["Dynamic Link", "link_name", "=", doc.name],
            ["disabled", "=", 0],
            ],
            pluck="name",
            limit=1,
        )
        contact=frappe.get_all(
            "Contact",
            filters=[
            ["Dynamic Link", "link_doctype", "=", 'Company'],
            ["Dynamic Link", "link_name", "=", doc.name],
            ],
            pluck="name",
            limit=1,
        )
        if address:
            new_cus.customer_primary_address = address[0]

        if contact:
            new_cus.customer_primary_contact =contact[0]

        new_cus.save()


    return 1

@frappe.whitelist()
def create_user(doc):
    doc = frappe.get_doc('Company',doc)
    for i in doc.user_table:
        update_user(i,doc)
    
    return 1

@frappe.whitelist()
def update_user_doc(i,doc):
    doc = frappe.get_doc('Company',doc)
    i = frappe.get_doc('Company Users',i)
    update_user(i,doc)

def update_user(i,doc):
    if not frappe.db.exists('User',{'email':i.email_id}):
        user = frappe.new_doc("User")
        user.email = i.email_id
        user.username = i.user_name
        user.first_name = i.user_name
        user.role_profile_name = i.role_profile
        user.enabled = i.enable
        user.new_password = i.get_password(fieldname="pswd")
        user.save()
    else:
        user = frappe.get_doc('User',{'email':i.email_id})
        user.update({
            'username': i.user_name,
            'first_name': i.user_name,
            'role_profile_name': i.role_profile,
            'enabled': i.enable,
            'new_password':i.get_password(fieldname="pswd")
        })
        user.save()

def delete_item_tax_template(doc,event):
    template = f' - {doc.abbr}'


    for i in frappe.get_all('Item Tax',{'item_tax_template':['like',f'%{template}']},pluck='name'):
        frappe.delete_doc('Item Tax',i)
        frappe.db.commit()
