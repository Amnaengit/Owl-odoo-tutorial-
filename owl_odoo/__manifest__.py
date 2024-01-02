# -*- coding: utf-8 -*-
{
    'name': "Owl Tutorial ",

    'summary': 'Owl Tutorial Development',
    'sequence': -1,
    'description': """
        OWL Tutotial
    """,

    'author': "Eng Amna Abdullah",
    'website': "https://www.owl.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'OWL',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','mail'],
    'license': 'LGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/todo_list.xml',
        'views/res_partner.xml',
        'views/odoo_services.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
           'owl_odoo/static/src/components/*/*.js',
           'owl_odoo/static/src/components/*/*.xml',
           'owl_odoo/static/src/components/*/*.scss',

        ],
    },
}
