# -*- coding: utf-8 -*-
{
    'name': "res_partner_extend",

    'summary': "Campos Adicionales en Contactos.",

    'description': """
Campos Adicionales en Contactos.
    """,

    'author': "Erick Escobar",
    'website': "",

    'category': 'CRM',
    'version': '0.1',

    'depends': ['contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ]
}

