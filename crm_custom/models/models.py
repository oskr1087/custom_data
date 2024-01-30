# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLoginData(models.Model):
    _name = 'crm.login.data'
    _inherit = [
        "portal.mixin",
        "mail.thread",
        "mail.activity.mixin",
    ]
    _description = 'Agregar registro de llamadas dentro del CRM'

    name = fields.Char(string="Nombre Cliente", required=True)
    date = fields.Date(string="Fecha Siguiente Llamada")
    date_to = fields.Datetime(string="Fecha/Hora Llamada", required=True)
    description = fields.Text(string="Observación",)

