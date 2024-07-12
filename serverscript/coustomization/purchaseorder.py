
import frappe
def send_notification_email(doc, method):
    supplier_email = "harshitchugh3125@gmail.com"
    if supplier_email:
        subject = f"Purchase Order {doc.name} Submitted"
        message = f"""
        <p>Dear {doc.supplier_name},</p>
        <p>Your purchase order {doc.name} has been submitted.</p>
        <p>Order Details:</p>
        <p><strong>Purchase Order:</strong> {doc.name}</p>
        <p><strong>Date:</strong> {doc.transaction_date}</p>
        <p><strong>Total Amount:</strong> {doc.grand_total}</p>
        <p>Please review the purchase order and confirm.</p>
        <p>Thank you,</p>
        <p>Your Company Name</p>
        """
        frappe.sendmail(recipients=supplier_email, subject=subject, message=message, delayed=False)