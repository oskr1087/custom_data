# -*- coding: utf-8 -*-
{
    'name': "res_partner_extend",

    'summary': "Campos y Menús Adicionales en Contactos.",

    'description': """
Campos y Menús Adicionales en Contactos.
    """,

    'author': "Erick Escobar",
    'website': "",

    'category': 'CRM',
    'version': '0.2',

    'depends': ['contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/relative.xml',
        'views/comm_channel.xml',
        'views/project.xml'                   
    ]
}

