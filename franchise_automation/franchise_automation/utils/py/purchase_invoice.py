import frappe

@frappe.whitelist()
def user_checking():

    company = frappe.get_value("User Permission", {"allow": "Company", "user": frappe.session.user}, "for_value")

    if company:

        company = frappe.get_doc("Company", company)

        if not company.is_group and company.parent_company:

            return True
        
        else:

            return False
        
    else:

        return False