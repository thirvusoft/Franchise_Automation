import frappe

from erpnext.accounts.doctype.sales_invoice.sales_invoice import update_taxes, make_inter_company_transaction

def on_submit(self, event):

    create_purchase_invoice(self)

def create_purchase_invoice(self):

    if frappe.get_value("Company", {"name": self.company}, "is_group"):

        new_doc = make_inter_company_transaction("Sales Invoice", source_name = self.name, target_doc = None)

        new_doc.save()