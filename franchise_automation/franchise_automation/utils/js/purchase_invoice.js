frappe.ui.form.on("Purchase Invoice", {

    refresh: function(frm){

        // if(frm.doc.__islocal){

        //     frappe.call({

        //         method: "franchise_automation.franchise_automation.utils.py.purchase_invoice.user_checking",

        //         callback:function(r){

        //             if(r.message){

        //                 frappe.msgprint("<b style='color:red'>Not Permitted</b> <b>To Create Purchase Invoice</b>.")
                        
        //                 frappe.set_route("Form", "Purchase Invoice")
        //             }
        //         }
        //     })
        // }
    }
})
