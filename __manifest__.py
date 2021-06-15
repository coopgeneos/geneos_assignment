# -*- coding: utf-8 -*-
{
    'name': "geneos assignment",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Geneos",
    'website': "http://www.geneos.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_groups.xml',
        'wizards/assignment_wizard_views.xml',
        'views/assignments_views.xml',
        'views/assignment_pivot_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}