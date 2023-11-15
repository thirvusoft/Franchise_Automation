frappe.ui.form.on('Company', {
	setup:function(frm,cdt,cdn){
        frm.set_query("account", "mode_of_payment", () => {
			return {
				filters: {
					company: frm.doc.name,
				},
			}
		});
    },
	update_mode_of_payment:async function(frm){
		if(await frm.is_dirty()){
			frm.save()
		}
		frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.create_mode',
			freeze: true,
			args: {
				'doc': frm.doc.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Updated Successfully'), indicator: 'green' });

			}
		})
	},
	update_item_tax_table:async function(frm){
		if(await frm.is_dirty()){
			frm.save()
		}
		frappe.show_alert({ message: __('Started Updating ..'), indicator: 'yellow' });
		frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.update_item_tax_table',
			// freeze: true,
			args: {
				'doc': frm.doc.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Updated Successfully'), indicator: 'green' });

			}
		})
	},
	create_customer_supplier:async function(frm){
		if(await frm.is_dirty()){
			frm.save()
		}
		frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.update_supplier',
			freeze: true,
			args: {
				'doc': frm.doc.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Created Successfully'), indicator: 'green' });

			}
		})
	},
	create_users:async function(frm){
		if(await frm.is_dirty()){
			frm.save()
		}
		frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.create_user',
			freeze: true,
			args: {
				'doc': frm.doc.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Created Successfully'), indicator: 'green' });

			}
		})
	}
});
frappe.ui.form.on('Company Users',{
	'create':async function(frm,cdt,cdn){
		if(await frm.is_dirty()){
			frm.save()
		}
		let row = locals[cdt][cdn]
		await frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.update_user_doc',
			freeze: true,
			args: {
				'doc': frm.doc.name,
				'i':row.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Created/Updated Successfully'), indicator: 'green' });

			}
		})
	}
})
