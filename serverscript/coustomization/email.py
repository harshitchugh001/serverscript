# Custom server script for Purchase Order doctype
import frappe

def on_submit(doc, method):
    send_supplier_notification(doc)

def send_supplier_notification(doc):
    supplier_email = frappe.db.get_value('Supplier', doc.supplier, 'email_id')
    if not supplier_email:
        frappe.throw(f'No email found for supplier {doc.supplier}')
    
    subject = f'Purchase Order {doc.name} Submitted'
    message = f'''
        <p>Dear Supplier,</p>
        <p>We have submitted a new Purchase Order <strong>{doc.name}</strong>.</p>
        <p>Please review the order details and confirm the delivery schedule.</p>
        <p>Thank you,</p>
        <p>{frappe.defaults.get_global_default('company')}</p>
    '''
    
    frappe.sendmail(
        recipients=supplier_email,
        subject=subject,
        message=message
    )

