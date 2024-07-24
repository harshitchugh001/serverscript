# Copyright (c) 2024, Harshit and contributors
# For license information, please see license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
class Testcustom_doc(FrappeTestCase):
    def setUp(self):
        # Create 
        print("setUp")
        self.doc = frappe.get_doc({
            "doctype": "custom_doc_test",
            "customer_name":"abc",
            "age":12,
            "mobile_no":1231231231
        }).insert()
        frappe.db.commit()
    def tearDown(self):
        # Delete 
        print("delete")
        if hasattr(self, 'doc') and self.doc.name:
            doc = frappe.get_doc('custom_doc_test', self.doc.name)
            doc.delete()
            frappe.db.commit()
    def test_check_field(self):
        # Verify 
        print("verify")
        doc = frappe.get_doc('custom_doc_test', self.doc.name)
        self.assertEqual(int(doc.age), 12)
    def test_update_field(self):
        # Update
        print("udate")
        doc = frappe.get_doc('custom_doc_test', self.doc.name)
        doc.age = 1
        doc.save() 
        frappe.db.commit()

        doc = frappe.get_doc('custom_doc_test', self.doc.name)
        self.assertEqual(int(doc.age), 1)