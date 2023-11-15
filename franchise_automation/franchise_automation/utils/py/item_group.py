import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def item_group_customisation():
    custom_field={
        "Item Group":[
             dict(
                fieldtype = "Column Break",
                fieldname= "column_break_1",
                insert_after = "is_group",
            ),
            dict(
                fieldname = "show_franchise",
                fieldtype = "Check",
                label = "Show to franchise",
                insert_after = "column_break_1",
            ),
             dict(
                fieldname = "restrict_franchise",
                fieldtype = "Check",
                label = "Restrict item creation by Franchise",
                insert_after = "show_franchise",
            ),
             dict(
                fieldname = "company",
                fieldtype = "Link",
                options = "Company",
                label = "Company",
                insert_after = "restrict_franchise",
                hidden = 1,
            )
        ],
        "Item":[
             dict(
                fieldname = "show_franchise_item",
                fieldtype = "Check",
                label = "Show to franchise",
                insert_after = "disabled",
                fetch_from = "item_group.show_franchise",
                fetch_if_empty=1,                
            ),            
             dict(
                fieldname = "restrict_franchise_item",
                fieldtype = "Check",
                label = "Restrict item creation by Franchise",
                insert_after = "show_franchise_item",
                fetch_from = "item_group.restrict_franchise",
                fetch_if_empty=1,
            ),
            dict(
                fieldname = "company",
                fieldtype = "Link",
                options= "Company",
                label = "Company",
                insert_after = "stock_uom",
                hidden=1            
            ),
            dict(
                fieldname = "company_is_group",
                fieldtype = "Check",
                label = "is_group",
                insert_after = "company",
                fetch_from = "company.is_group",
                hidden=1  
            )
        ]
    }   
    create_custom_fields(custom_field)

def property_setter():
    make_property_setter("Item", "serial_nos_and_batches", "depends_on", "eval:doc.is_stock_item && doc.is_group", "Data")