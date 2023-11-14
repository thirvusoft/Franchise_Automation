import frappe

def on_submit(self, event):

    create_sales_order(self)

def create_sales_order(self):

    parent_company = frappe.get_value("Company", {"name": self.company}, "parent_company")

    if parent_company:

        if frappe.db.exists("Customer", {"name": self.supplier}):

            pass