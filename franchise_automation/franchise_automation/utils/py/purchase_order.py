import frappe

def on_submit(self, event):

    create_sales_order(self)

def create_sales_order(self):

    parent_company = frappe.get_value("Company", {"name": self.company}, "parent_company")

    if parent_company:

        if frappe.db.exists("Customer", {"name": self.supplier}):

            new_doc = frappe.new_doc("Sales Order")

            new_doc.customer = self.supplier

            new_doc.company = parent_company

            new_doc.transaction_date = self.transaction_date

            new_doc.delivery_date = self.schedule_date

            for item in self.items:

                new_doc.append("items",{
                    "item_code": item.item_code,
                    "delivery_date": item.schedule_date,
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

            new_doc.save()

        else:

            frappe.throw(f"Customer name {self.supplier} is not found.", title = "Message")