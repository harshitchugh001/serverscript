// Copyright (c) 2024, Harshit and contributors
// For license information, please see license.txt

frappe.ui.form.on("program2", {
	refresh(frm) {

        frm.add_custom_button(__('Add New Item'), function() {
            open_add_new_item_dialog(frm);
        });
        
        

	},
});

function open_add_new_item_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: __('Add New Item'),
        fields: [
            {
                fieldname: 'item_group',
                label: __('Item Group'),
                fieldtype: 'Link',
                options: 'Item Group',
                reqd: 1,
                change: function() {
                    
                    d.get_field('item').get_query = function() {
                        return {
                            filters: {
                                'item_group': d.get_value('item_group')
                            }
                        };
                    };
                }
            },
            {
                fieldname: 'item',
                label: __('Item'),
                fieldtype: 'Link',
                options: 'Item',
                reqd: 1,
                change: function() {
                    frappe.db.get_value('Item', d.get_value('item'), 'item_name', function(value) {
                        d.set_value('item_name', value.item_name);
                    });
                }
            },
            {
                fieldname: 'item_name',
                label: __('Item Name'),
                fieldtype: 'Data',
                read_only: 1
            },
            
        ],
        primary_action_label: __('Add Item'),
        primary_action(values) {
            if (validate_dialog_values(values)) {
                let new_item = frm.add_child('program_items');
                new_item.item_group = values.item_group;
                new_item.item = values.item;
                

                frm.refresh_field('program_items');
                d.hide();
                frappe.msgprint(__('Item added successfully'));
            } else {
                frappe.msgprint(__('Please fill all required fields'));
            }
        }
    });
    d.show();
}


function validate_dialog_values(values) {
    return values.item_group && values.item ;
}

