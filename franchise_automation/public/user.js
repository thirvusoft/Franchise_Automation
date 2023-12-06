frappe.ui.form.UserQuickEntryForm = class UserQuickEntryForm extends (frappe.ui.form.UserQuickEntryForm ? frappe.ui.form.UserQuickEntryForm : frappe.ui.form.QuickEntryForm) {
   render_dialog() {
        super.render_dialog();
        this.doc.__parent_company_user_permission__ = 1;
   }
}
