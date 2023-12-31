from . import __version__ as app_version

app_name = "franchise_automation"
app_title = "Franchise Automation"
app_publisher = "Thirvusoft"
app_description = "Automate the franchise configuration"
app_email = "ts@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/franchise_automation/css/franchise_automation.css"
app_include_js = ["/assets/franchise_automation/user.js"]

# include js, css files in header of web template
# web_include_css = "/assets/franchise_automation/css/franchise_automation.css"
# web_include_js = "/assets/franchise_automation/js/franchise_automation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "franchise_automation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Invoice" : "franchise_automation/utils/js/purchase_invoice.js",
    "Company" : "franchise_automation/utils/js/company.js",
    "User": "franchise_automation/utils/js/user.js",
  }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "franchise_automation.utils.jinja_methods",
#	"filters": "franchise_automation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "franchise_automation.install.before_install"
# after_install = "franchise_automation.install.after_install"

after_migrate = "franchise_automation.install.after_migrate"
# Uninstallation
# ------------

# before_uninstall = "franchise_automation.uninstall.before_uninstall"
after_install = "franchise_automation.franchise_automation.utils.py.custom_field.custom_naming"


# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "franchise_automation.utils.before_app_install"
# after_app_install = "franchise_automation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "franchise_automation.utils.before_app_uninstall"
# after_app_uninstall = "franchise_automation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "franchise_automation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Role Profile": "franchise_automation.franchise_automation.utils.py.user.role_profile_permission",
}
#
has_permission = {
	"Role Profile": "franchise_automation.franchise_automation.utils.py.user.has_role_profile_permission",
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Purchase Order": {
		"on_submit": "franchise_automation.franchise_automation.utils.py.purchase_order.on_submit",
    "on_cancel": "franchise_automation.franchise_automation.utils.py.purchase_order.on_cancel",
    "before_naming":"franchise_automation.franchise_automation.utils.py.naming_series.set_purchase_name"
	},
  
  ('Stock Entry','Stock Reconciliation','Material Request','Quotation','Journal Entry','Payment Entry'): {
        "before_naming":"franchise_automation.franchise_automation.utils.py.naming_series.naming_series"

	},
    ('Purchase Invoice','Purchase Receipt','Delivery Note','Sales Order'): {
		"before_naming":"franchise_automation.franchise_automation.utils.py.naming_series.set_purchase_name"
	},

	'Company':{
		"validate": "franchise_automation.franchise_automation.utils.py.company.validate",
		'on_trash': "franchise_automation.franchise_automation.utils.py.company.delete_item_tax_template",
		'after_insert': "franchise_automation.franchise_automation.utils.py.company.after_insert"

  	},
 
    "Item Group": {
        "validate": "franchise_automation.franchise_automation.utils.py.item.update_company_in_item_from_item_group"
	},
    "Item": {
        "validate": "franchise_automation.franchise_automation.utils.py.item.validate_company_in_item"
    },
  
  "Sales Invoice": {
		"on_submit": "franchise_automation.franchise_automation.utils.py.sales_invoice.on_submit",
    "on_cancel": "franchise_automation.franchise_automation.utils.py.sales_invoice.on_cancel",
    "before_naming":"franchise_automation.franchise_automation.utils.py.naming_series.naming_sales_invoice"
	},
  "Stock Ledger Entry": {
     "autoname":"franchise_automation.franchise_automation.utils.py.naming_series.stock_ledger_entry"
	},
  "User": {
      "after_insert": "franchise_automation.franchise_automation.utils.py.user.create_user_permission"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"franchise_automation.tasks.all"
#	],
#	"daily": [
#		"franchise_automation.tasks.daily"
#	],
#	"hourly": [
#		"franchise_automation.tasks.hourly"
#	],
#	"weekly": [
#		"franchise_automation.tasks.weekly"
#	],
#	"monthly": [
#		"franchise_automation.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "franchise_automation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "franchise_automation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "franchise_automation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["franchise_automation.utils.before_request"]
# after_request = ["franchise_automation.utils.after_request"]

# Job Events
# ----------
# before_job = ["franchise_automation.utils.before_job"]
# after_job = ["franchise_automation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"franchise_automation.auth.validate"
# ]
