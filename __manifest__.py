# -*- coding: utf-8 -*-
{
    'name': "fix_inventory_line_constraint",

    'summary': """
     Fixes inventory line constraint. Current inventory line constraint does not allow multiple lines per product""",
    'description': """
     Fixes inventory line constraint. Current inventory line constraint does not allow multiple lines per product""",
    'author': "Moldeo Interactive",
    'website': "https://www.moldeointeractive.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
