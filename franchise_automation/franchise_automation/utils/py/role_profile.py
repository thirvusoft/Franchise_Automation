import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def role_profile_customisation():
    custom_fields = {
        "Role Profile": [
            dict(fieldname='col', label='',
                fieldtype='Column Break',insert_after='role_profile'),
            dict(fieldname='applicable_for_child_company', label='Applicable for Child Company',
                fieldtype='Check',insert_after='col'),
            dict(fieldname='sec', label='',
                fieldtype='Section Break',insert_after='applicable_for_child_company'),
         ],
            
    }
    create_custom_fields(custom_fields)