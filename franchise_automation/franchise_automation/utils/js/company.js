frappe.ui.form.on('Company', {
	setup:function(frm,cdt,cdn){
        frm.set_query("account", "mode_of_payment", () => {
			return {
				filters: {
					company: frm.doc.name,
				},
			}
		});
		frm.set_query("role_profile", "user_table", () => {
			return {
				query: "franchise_automation.franchise_automation.utils.py.company.child_role_profile",
				
			
			};
			// return {
			
		});
    },
	custom_disable:function(frm){
		frm.set_value('custom_trigger_disable',1)
	},
	refresh:function(frm){
		frm.add_custom_button(__('Update Item Tax Table'), () =>{
            frm.trigger("update_item_tax_table");
         });
	},
	update_mode_of_payment:async function(frm){
		if(await frm.is_dirty()){
			await frm.save()
		}
		await frappe.call({
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
			await frm.save()
		}
		frappe.show_alert({ message: __('Started Updating ..'), indicator: 'yellow' });
		await frappe.call({
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
	create_pos:async function(frm){
		if(await frm.is_dirty()){
			await frm.save()
		}
		await frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.create_pos',
			freeze: true,
			args: {
				'doc': frm.doc.name
			},
			callback: function(r) {
				if(r.message == 1){
					frappe.show_alert({ message: __('Created Successfully'), indicator: 'green' });

				}
				else{
					frappe.show_alert({ message: __('Already Created ..!'), indicator: 'green' });

				}
			}
		})
	},
	create_customer_supplier:async function(frm){
		if(await frm.is_dirty()){
			await frm.save()
		}
		await frappe.call({
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
			await frm.save()
		}
		await frappe.call({
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
		let row = locals[cdt][cdn]

		if(await cur_frm.is_dirty()){
			await cur_frm.save()
		}
		await frappe.call({
			method: 'franchise_automation.franchise_automation.utils.py.company.update_user_doc',
			freeze: true,
			args: {
				'doc': cur_frm.doc.name,
				'i':row.name
			},
			callback: function(r) {
				frappe.show_alert({ message: __('Created/Updated Successfully'), indicator: 'green' });

			}
		})
	}
})
