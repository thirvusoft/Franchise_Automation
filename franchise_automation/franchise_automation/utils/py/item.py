import frappe

def update_company_in_item_from_item_group(doc, event = None):
    if not doc.get("_doc_before_save") or (doc.show_franchise != doc._doc_before_save.show_franchise):
        parent_company = frappe.db.get_value("Company", {"is_group": 1, "parent_company": ["is", "not set"]}, "name")

        if doc.show_franchise:
            doc.company = ''
        elif not doc.company:
            doc.company = parent_company

        for item in frappe.get_all("Item", {"item_group": doc.name}, pluck="name"):
            frappe.db.set_value("Item", item, {
                "show_franchise_item": doc.show_franchise,
                "company": ("" if doc.show_franchise else parent_company)
            })


def validate_company_in_item(doc, event = None):
    if doc.show_franchise_item:
        doc.company = ''
    elif not doc.company:
        doc.company = frappe.db.get_value("Company", {"is_group": 1, "parent_company": ["is", "not set"]}, "name")
