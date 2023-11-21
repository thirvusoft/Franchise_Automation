
import frappe
from frappe.model.naming import parse_naming_series
from erpnext.accounts.utils import get_fiscal_year

doctype_prefix_mapping = {
    'Stock Entry': 'STE',
    'Stock Reconciliation': 'RECO',
    'Material Request':'MR',
    'Quotation':'QUOT',
    'Journal Entry':'JE',
    'Payment Entry':'PAY',
}

def set_document_name(doc):
    abb = frappe.db.get_value('Company', doc.company, 'abbr')
    doctype = frappe.get_value('DocType', doc.doctype, 'name')
    prefix = doctype_prefix_mapping.get(doctype, '')
    doc.custom_naming_series = (f"{abb}-{prefix}")


def naming_series(doc, action):
    set_document_name(doc)


def stock_ledger_entry(doc,event):
    abb = frappe.db.get_value('Company', doc.company, 'abbr')
    prefix = 'SLE'
    doc.name = parse_naming_series(f"{abb}-{prefix}-.###")


def get_fiscal_year_short_form():
    a=[]
    fy =  frappe.db.get_single_value('Global Defaults', 'current_fiscal_year')    
    fy1 =  frappe.db.get_single_value('Global Defaults', 'current_fiscal_year') 
    a.append(fy.split('-')[0][2:] )
    a.append(fy1.split('-')[1][2:] )

    return a


def naming_sales_invoice(doc, action):  
    a = get_fiscal_year_short_form()
    abb = frappe.db.get_value('Company', doc.company, 'abbr')
    doc.custom_naming_series = f"{abb}{a[0]}{a[1]}"
    if doc.is_return:
        doc.naming_series= "{custom_naming_series}.-.###.-R"
    else:
        doc.naming_series= "{custom_naming_series}.-.###"


doctype_prefix_mapping_return = {
    'Purchase Invoice': 'PI',
    'Purchase Order': 'PO',
    'Purchase Receipt': 'PR',
    'Delivery Note':'DN',
    'Sales Order':'SO'
}

def set_purchase_name(doc,event):
    a = get_fiscal_year_short_form()
    abb = frappe.db.get_value('Company', doc.company, 'abbr')
    doctype = frappe.get_value('DocType', doc.doctype, 'name')
    prefix = doctype_prefix_mapping_return.get(doctype, '')
    doc.custom_naming_series = f"{abb}{a[0]}{a[1]}{prefix}"
    if doc.get('is_return'):
        doc.naming_series= "{custom_naming_series}.-.###.-R"
    else:
        doc.naming_series= "{custom_naming_series}.-.###"
