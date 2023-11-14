import frappe
from franchise_automation.utils.py.company import company_customisation
def after_migrate():
    company_customisation()