import frappe
import frappe.utils
def validate(doc, method):
    if doc.custom_customer_anniversary and doc.custom_customer_anniversary > frappe.utils.today():
        frappe.throw(("Customer Anniversary cannot be a future date."))