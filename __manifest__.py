# -*- coding: utf-8 -*-
{
    'name': "dragonball_z",

    'summary': """
        Modulo de Dragon Ball Z""",

    'description': """
        Modulo de Dragon Ball Z
    """,

    'author': "Antonio Olmo Lopez",
    'website': "https://www.a2mkt.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ciencia ficcion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/terricolas.xml',
        'views/namekiano.xml',
        'views/superheroe.xml',
        #'views/dios.xml',
        'reportes/informes_terricolas.xml',
        #'reportes/informes_dios.xml',
        'reportes/informes_superheroe.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}