import frappe

def create_user_permission(doc, event=None):
    if doc.get("__parent_company_user_permission__"):
        company = frappe.db.get_value("Company", {'is_group': 1, 'parent_company': ['is', 'not set']})
        user_perm = frappe.new_doc("User Permission")
        user_perm.update({
            "user": doc.name,
            "allow": "Company",
            "for_value": company,
            "apply_to_all_doctypes": 1,
        })
        user_perm.save()

def role_profile_permission(user):
    if not user:
        user = frappe.session.user
    
    child_company = 1
    if frappe.db.get_list("Company", {"is_group": 1}):
        child_company = 0
    
    return f"""(`tabRole Profile`.applicable_for_child_company = {child_company})"""
