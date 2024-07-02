

import frappe

from frappe import _


@frappe.whitelist()

def get_items():
    if(frappe.local.request.method != "GET"):
        
        return "only GET request is accepted"
    doctype = frappe.local.form_dict.get('doctype')
    name = frappe.local.form_dict.get("name")
    if not doctype:
        return {"error": "Required :- doctype "}, 400

    if(name):
        try:
            item = frappe.get_doc(doctype, name)
            return item
        except Exception as e:
            return {"error": str(e)}, 500
        
    all_items=[]
   
    try:
        records = frappe.get_all(doctype, fields=["*"])
        for record in records:
            all_items.append(frappe.get_doc(doctype,record))
        return all_items
    except Exception as e:
        return {"error": str(e)}, 500


@frappe.whitelist()
def create_item():
    if(frappe.local.request.method != "POST"):
        
        return "only POST request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    if not doctype:
        return {"error": "Required :- doctype"}, 400

    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500



@frappe.whitelist()
def update_item(allow_guest = True):
    if(frappe.local.request.method != "PUT"):
        
        return "only PUT request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "Required :- doctype and name "}, 400

    try:
        doc = frappe.get_doc(doctype, name)
        doc.update(data)
        doc.save()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500



@frappe.whitelist()
def delete_item():
    if(frappe.local.request.method != "DELETE"):
        
        return "only DELETE request is accepted"
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "!Required:- doctype and name"}, 400

    try:
        frappe.delete_doc(doctype, name)
        return {"message": f"Item {name} deleted successfully"}
    except Exception as e:
        return {"error": str(e)}, 500
    


@frappe.whitelist(allow_guest = True)
def get_users():
    return frappe.get_all("User",fields=["*"])


@frappe.whitelist()
def add_user():
    if(frappe.local.request.method != "POST"):
        # frappe.throw("only post request si accepted")
        return "only POST request is accepted"
    data = frappe.local.form_dict
    try:
        user = frappe.get_doc({"doctype":"User",**data})
        user.insert()
        frappe.db.commit()
        return user.as_dict()
    except Exception as e:
        return {"error": str(e)},500