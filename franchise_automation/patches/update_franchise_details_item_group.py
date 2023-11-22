import frappe
from franchise_automation.franchise_automation.utils.py.item import update_company_in_item_from_item_group

def execute():
    for ig in frappe.get_all("Item Group"):
        doc = frappe.get_doc("Item Group", ig.name)
        update_company_in_item_from_item_group(doc)
        doc.db_update()
