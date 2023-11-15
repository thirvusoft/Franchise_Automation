import frappe

from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_inter_company_transaction

def on_submit(self, event):

	create_sales_order(self)

def create_sales_order(self):

	if frappe.get_value("Company", {"name": self.company}, "parent_company"):

		new_doc =  make_inter_company_transaction("Purchase Order", source_name = self.name, target_doc = None)

		new_doc.delivery_date = self.schedule_date

		new_doc.save()