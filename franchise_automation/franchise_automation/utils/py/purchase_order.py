import frappe

from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_inter_company_transaction

def on_submit(self, event):

	create_sales_order(self)
	  
def on_cancel(self, event):

	cancel_inter_company_so(self)

def create_sales_order(self):

	if frappe.get_value("Company", {"name": self.company}, "parent_company"):

		new_doc =  make_inter_company_transaction("Purchase Order", source_name = self.name, target_doc = None)

		new_doc.delivery_date = self.schedule_date

		new_doc.save()

def cancel_inter_company_so(self):
	
	if frappe.db.exists("Sales Order", {"inter_company_order_reference": self.name}):
						
		doc = frappe.get_doc("Sales Order", {"inter_company_order_reference": self.name})

		if doc.docstatus == 0:

			frappe.delete_doc("Sales Order", doc.name, ignore_permissions = True)