# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "OA",
    "summary": "Modulo Open Academy",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://odoo-community.org/",
    "author": "Leezao, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
   # "pre_init_hook": "pre_init_hook",
   # "post_init_hook": "post_init_hook",
   # "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "data": [
        "views/course.xml",
    #    "security/some_model_security.xml",
    #    "security/ir.model.access.csv",
    #    "views/assets.xml",
    #    "views/report_name.xml",
    #    "views/res_partner_view.xml",
    #    "wizard/wizard_model_view.xml",
    ],
    "demo": [
    #    "demo/res_partner_demo.xml",
    ],
    "qweb": [
    #    "static/src/xml/module_name.xml",
    ]
}
