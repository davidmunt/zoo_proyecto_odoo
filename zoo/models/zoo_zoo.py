# -*- coding: utf-8 -*-

from datetime import date
from odoo.exceptions import UserError
from odoo import models, fields, api

class Zoo(models.Model):
    _name = 'zoo.zoo'

    name = fields.Char(required=True, String="Nombre")
    ciudad = fields.Char(required=True, String="Ciudad")
    pais_id = fields.Many2one('res.country', string='Pais')
    superficie = fields.Float(required=True, default=0, String="Superficie (m²)")
    animales_ids = fields.One2many("zoo.animal", "zoo_id", string="Animales")
    fecha_fund = fields.Date(required=True, store=True, string="Fecha de fundacion")
    logo = fields.Image(string="Logo")
    cant_animales = fields.Integer(string="Cantidad de animales", compute="_compute_cant_anim")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    tiene_animales_vivos = fields.Boolean(string="Tiene Animales Vivos", compute="_compute_tiene_animales_vivos")
    
    @api.constrains('superficie')
    def _verify_fechaNac(self):
        for record in self:
            if record.superficie <= 0:
                raise UserError('La superficie no puede ser igual a cero o un numero negativo')
                
    @api.constrains('fecha_fund')
    def _verificar_fechaFund(self):
        for record in self:
            ahora = date.today()
            if record.fecha_fund and record.fecha_fund > ahora:
                raise UserError('La fecha de fundacion no puede estar en el futuro')
                
    @api.depends('animales_ids')
    def _compute_tiene_animales_vivos(self):
        for record in self:
            record.tiene_animales_vivos = any(record.animales_ids.filtered(lambda a: a.estado != 'fallecido'))
                
    @api.depends('animales_ids')
    def _compute_cant_anim(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales = len(record.animales_ids.filtered(lambda a: a.estado != 'fallecido'))
            else:
                record.cant_animales = 0