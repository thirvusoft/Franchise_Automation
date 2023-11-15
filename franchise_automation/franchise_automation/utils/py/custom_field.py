import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def custom_naming():
    custom_field_list()
    property_setter()

def custom_field_list():
    custom_field={
        "Stock Entry":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "stock_entry_type",
                hidden=1
                
            ),
        ],
         "Stock Reconciliation":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "purpose",
                hidden=1

                
            ),
        ],
        "Stock Ledger Entry":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "naming_series",
                hidden=1
            ),
            dict(
                fieldname = "naming_series",
                fieldtype = "Select",
                options = '{custom_naming_series}.-.###',
                label = "Naming Series",
                insert_after = "item_code",
                hidden=1,
                default='{custom_naming_series}.-.###'
            ),
        ],
          "Material Request":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "company",
                hidden=1
           
            ),
        ],
          "Quotation":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "quotation_to",
                hidden=1
           
            ),
        ],
        "Journal Entry":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "voucher_type",
                hidden=1
           
            ),
        ],
        "Payment Entry":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "payment_type",
                hidden=1
           
            ),
        ],
        "Purchase Invoice":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "supplier",
                hidden=1

            ),
        ],

        "Purchase Order":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "supplier",
                hidden=1

            ),
        ],
        "Purchase Receipt":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "supplier",
                hidden=1

            ),
        ],
        "Delivery Note":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "customer",
                hidden=1

            ),
        ],
        "Sales Order":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "customer",
                hidden=1

            ),
        ],
        "Sales Invoice":[
             dict(
                fieldname = "custom_naming_series",
                fieldtype = "Data",
                label = "Naming Series",
                insert_after = "customer",
                hidden=1

            ),
        ],
    }   
    create_custom_fields(custom_field)

def property_setter():
    make_property_setter('Stock Entry', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Stock Entry', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Stock Reconciliation', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Stock Reconciliation', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Stock Ledger Entry', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Stock Ledger Entry', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Stock Ledger Entry',"","autoname", 'field:custom_naming_series', "Data",for_doctype=True)
    make_property_setter('Stock Ledger Entry',"","naming_rule", 'By "Naming Series" field', "Data",for_doctype=True)


    make_property_setter('Material Request', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Material Request', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Quotation', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Quotation', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Journal Entry', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Journal Entry', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")


    make_property_setter('Payment Entry', "naming_series", "options", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Payment Entry', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Purchase Invoice', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Purchase Invoice', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")
    make_property_setter('Purchase Invoice', "represents_company", "ignore_user_permissions", 1, "Check")



    make_property_setter('Purchase Order', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Purchase Order', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Purchase Receipt', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Purchase Receipt', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    make_property_setter('Delivery Note', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Delivery Note', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")


    make_property_setter('Sales Order', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Sales Order', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")


    make_property_setter('Sales Invoice', "naming_series", "options", '''{custom_naming_series}.-.###\n{custom_naming_series}.-.###.-R''', "Small Text",validate_fields_for_doctype=False)
    make_property_setter('Sales Invoice', "naming_series", "default", '''{custom_naming_series}.-.###''', "Small Text")

    frappe.db.commit()