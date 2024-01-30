# -*- coding: utf-8 -*-
{
    'name': "Personalizaciones para el CRM (ERIK)",

    'summary': "Agregar campos extras en el CRM",

    'description': """
Agregar campos extras en el CRM
    """,

    'author': "Erik Escobar <om@prisehub.com>",
    'website': "https://www.prisehub.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tool',
    'version': '17.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/crm_groups.xml',
        'security/ir.model.access.csv',
        'views/views_crm_custom.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
}

