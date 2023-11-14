import frappe

from erpnext.accounts.doctype.sales_invoice.sales_invoice import update_taxes

def on_submit(self, event):

    create_purchase_invoice(self)

def create_purchase_invoice(self):

    if frappe.get_value("Company", {"name": self.company}, "is_group"):

        if frappe.db.exists("Supplier", {"name": self.customer}):

            represents_company = frappe.get_value("Customer", {"name": self.customer}, "represents_company")
            
            if represents_company:

                new_doc = frappe.new_doc("Purchase Invoice")

                new_doc.supplier = self.customer

                new_doc.company = represents_company

                new_doc.posting_date = self.posting_date

                new_doc.due_date = self.due_date

                new_doc.update_stock = 0

                for item in self.items:

                    new_doc.append("items", {
                        "item_code": item.item_code,
                        "qty": item.qty,
                        "rate": item.rate,
                        "uom": item.uom,
                        "margin_type": item.margin_type,
                        "margin_rate_or_amount": item.margin_rate_or_amount,
                        "discount_percentage": item.discount_percentage,
                        "discount_amount": item.discount_amount,
                        "item_tax_template": item.item_tax_template
                    })

                new_doc.tax_category = self.tax_category

                new_doc.additional_discount_percentage = self.additional_discount_percentage

                new_doc.discount_amount = self.discount_amount

                new_doc.apply_discount_on = self.apply_discount_on

                new_doc.disable_rounded_total = self.disable_rounded_total

                new_doc.rounding_adjustment = self.rounding_adjustment

                new_doc.set_missing_values()

                update_taxes(
                    doc = new_doc,
                    party = new_doc.supplier,
                    party_type = "Supplier",
                    company = new_doc.company,
                    doctype = new_doc.doctype,
                    party_address = new_doc.supplier_address,
                    company_address = new_doc.shipping_address
			    )

                new_doc.save()

        else:

            frappe.throw(f"Supplier name {self.customer} is not found.", title = "Message")