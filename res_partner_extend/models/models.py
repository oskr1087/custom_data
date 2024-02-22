# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.tools.date_utils
from odoo.exceptions import UserError, ValidationError
 
#Datos Maestros
class ResPartnerProject(models.Model):
    _name = 'res.partner.project'
    #Campos
    name = fields.Char(string = 'Proyecto', required = True)
    shortcut = fields.Char(string = 'Abreviatura', required = True)

class ResPartnerCommChannel(models.Model):
    _name = 'res.partner.comm.channel'
    #Campos
    name = fields.Char(string = 'Canal de Comunicación', required = True)
    shortcut = fields.Char(string = 'Abreviatura', required = True)
   
class ResPartnerRelative(models.Model):
    _name = 'res.partner.relative'
    #Campos
    name = fields.Char(string = 'Parentesco', required = True)
    shortcut = fields.Char(string = 'Abreviatura', required = True)

#Detalles
class ResPartnerRelativeDetails(models.Model):
    _name = 'res.partner.relative.details'
    #Campos
    relative = fields.Many2one('res.partner', string = 'Familiar', required = True)
    kinship = fields.Many2one('res.partner.relatives', string = 'Parentesco', required = True)    
    partner_id = fields.Many2one('res.partner', string = 'Contacto')

class ResPartnerMailDetails(models.Model):
    _name = 'res.partner.mail.details'
    #Campos
    mail = fields.Char(string = 'Correo Electrónico', required = True)
    partner_id = fields.Many2one('res.partner',string = 'Contacto')

class ResPartnerPhoneDetails(models.Model):
    _name = 'res.partner.phone.details'
    #Campos
    name = fields.Char(string = 'Teléfono', required = True)
    partner_id = fields.Many2one('res.partner',string = 'Contacto')   

class ResPartner(models.Model):
    _inherit = 'res.partner'    
    #Campos con Dependencia
    partner_email_id = fields.One2many('res.partner.email.details', 'partner_id', string = 'Detalle de Correos Electrónicos Adicionales')
    partner_phone_id = fields.One2many('res.partner.phone.details', 'partner_id', string = 'Detalle de Teléfonos Adicionales')
    partner_relative_id = fields.One2many('res.partner.relative.details', 'partner_id', string = 'Detalle de Familiares')
    comm_channel = fields.One2many('res.partner.comm.channel', 'project', string = 'Canal de Comunicación')
    project = fields.One2many('res.partner.project', 'project', string = 'Proyecto')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, readonly = True)
    #Campos
    budget = fields.Monetary(string = 'Presupuesto', currency_id = currency_id)
    income = fields.Monetary(string = 'Ingresos', currency_id = currency_id)
    contact_date = fields.Date(string = 'Fecha de Contacto', readonly = True)


