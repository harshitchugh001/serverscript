# Copyright (c) 2024, Harshit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class myschedular(Document):
	pass



@frappe.whitelist()
def update_counter():
		schedules = frappe.get_all('myschedular', filters={})
		for schedule in schedules:
			doc = frappe.get_doc('myschedular', schedule.name)
			doc.count = doc.count + 1
			doc.save()
			frappe.db.commit()
			print("Counter updated for all myschedule documents")
			return doc.count
