import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

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

            #  dict(
            #     fieldtype = "Column Break",
            #     fieldname= "column_break_2",
            #     insert_after = "show_franchise",
                
            # ),
             dict(
                fieldname = "restrict_franchise",
                fieldtype = "Check",
                label = "Restrict item creation by Franchise",
                insert_after = "show_franchise",
                
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
                
            )
        ]
    }   
    create_custom_fields(custom_field)