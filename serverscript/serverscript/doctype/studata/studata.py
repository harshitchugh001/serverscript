# Copyright (c) 2024, Harshit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class studata(Document):
	def after_insert(self):
		frappe.sendmail(recipients={self.email},subject="new account",message=f"welcome {self.name}",delayed=False)
