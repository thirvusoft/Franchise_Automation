frappe.ui.form.on("User", {
    refresh: async function(frm) {
        if (frm.is_new()) {
            frm.doc.__parent_company_user_permission__ = 1
        }
    }
});
