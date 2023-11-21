import frappe

from erpnext.accounts.doctype.sales_invoice.sales_invoice import update_taxes, make_inter_company_transaction

def on_submit(self, event):

    create_purchase_invoice(self)

def on_cancel(self, event):

    cancel_inter_company_pi(self)

def create_purchase_invoice(self):

    if frappe.get_value("Company", {"name": self.company}, "is_group") and frappe.get_value("Customer", {"name": self.customer}, "is_internal_customer") :

        new_doc = make_inter_company_transaction("Sales Invoice", source_name = self.name, target_doc = None)

        new_doc.save()

def cancel_inter_company_pi(self):

    if frappe.db.exists("Purchase Invoice", {"inter_company_invoice_reference": self.name}):
                        
        doc = frappe.get_doc("Purchase Invoice", {"inter_company_invoice_reference": self.name})

        if doc.docstatus == 0:
            frappe.delete_doc("Purchase Invoice", doc.name, ignore_permissions = True)