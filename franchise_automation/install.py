import frappe
from franchise_automation.utils.py.company import company_customisation
from franchise_automation.franchise_automation.utils.py.item_group import item_group_customisation
def after_migrate():
    company_customisation()
    item_group_customisation()