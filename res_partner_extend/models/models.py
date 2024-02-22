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
    kinship = fields.Many2one('res.partner.relative', string = 'Parentesco', required = True)    
    res_partner_id = fields.Many2one('res.partner', string = 'Contacto')

class ResPartneremailDetails(models.Model):
    _name = 'res.partner.email.details'
    #Campos
    email = fields.Char(string = 'Correo Electrónico', required = True)
    res_partner_id = fields.Many2one('res.partner',string = 'Contacto')

class ResPartnerPhoneDetails(models.Model):
    _name = 'res.partner.phone.details'
    #Campos
    phone = fields.Char(string = 'Teléfono', required = True)
    res_partner_id = fields.Many2one('res.partner',string = 'Contacto')   

class ResPartner(models.Model):
    _inherit = 'res.partner'    
    #Campos con Dependencia
    res_partner_email_id = fields.One2many('res.partner.email.details', 'res_partner_id', string = 'Detalle de Correos Electrónicos Adicionales')
    res_partner_phone_id = fields.One2many('res.partner.phone.details', 'res_partner_id', string = 'Detalle de Teléfonos Adicionales')
    res_partner_relative_id = fields.One2many('res.partner.relative.details', 'res_partner_id', string = 'Detalle de Familiares')
    comm_channel = fields.One2many('res.partner.comm.channel', 'name', string = 'Canal de Comunicación')
    project = fields.One2many('res.partner.project', 'name', string = 'Proyecto')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, readonly = True)
    #Campos
    budget = fields.Monetary(string = 'Presupuesto', currency_id = currency_id)
    income = fields.Monetary(string = 'Ingresos', currency_id = currency_id)
    contact_date = fields.Date(string = 'Fecha de Contacto', readonly = True)


