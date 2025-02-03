# -*- coding: utf-8 -*-

from datetime import date
from odoo.exceptions import UserError
from odoo import models, fields, api

class Zoo(models.Model):
    _name = 'zoo.zoo'

    name = fields.Char(required=True, String="Nombre")
    direccion = fields.Char(required=True, String="Direccion")
    ciudad = fields.Char(required=True, String="Ciudad")
    pais_id = fields.Many2one('res.country', string='Pais', required=True)
    provincia_id = fields.Many2one('res.country.state', string='Provincia', required=True)
    superficie = fields.Float(required=True, default=0, String="Superficie (m²)")
    animales_ids = fields.One2many("zoo.animal", "zoo_id", string="Animales")
    etiqueta_ids = fields.Many2many("zoo.etiqueta", "zoo_id", string="Etiquetas")
    fecha_fund = fields.Date(required=True, store=True, string="Fecha de fundacion")
    logo = fields.Image(string="Logo")
    cant_animales = fields.Integer(string="Cantidad de animales", compute="_compute_cant_anim")
    cant_animales_disponible = fields.Integer(string="Animales disponibles", compute="_compute_cant_anim_disponible")
    cant_animales_enfermo = fields.Integer(string="Animales enfermos", compute="_compute_cant_anim_enfermo")
    cant_animales_herv = fields.Integer(string="Cantidad de animales hervivoros", compute="_compute_cant_anim_herv")
    cant_animales_carn = fields.Integer(string="Cantidad de animales carnivoros", compute="_compute_cant_anim_carn")
    cant_animales_omni = fields.Integer(string="Cantidad de animales omnivoros", compute="_compute_cant_anim_omni")
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
                
    @api.depends('animales_ids')
    def _compute_cant_anim_disponible(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales_disponible = len(record.animales_ids.filtered(lambda a: a.estado == 'disponible'))
            else:
                record.cant_animales_disponible = 0
                
    @api.depends('animales_ids')
    def _compute_cant_anim_enfermo(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales_enfermo = len(record.animales_ids.filtered(lambda a: a.estado == 'enfermo'))
            else:
                record.cant_animales_enfermo = 0
                
    @api.depends('animales_ids', 'animales_ids.estado', 'animales_ids.especie_id')
    def _compute_cant_anim_herv(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales_herv = len(record.animales_ids.filtered(lambda a: a.estado != 'fallecido' and a.especie_id.tipo_alimentacion == 'hervivoro'))
            else:
                record.cant_animales_herv = 0
    
    @api.depends('animales_ids', 'animales_ids.estado', 'animales_ids.especie_id')
    def _compute_cant_anim_carn(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales_carn = len(record.animales_ids.filtered(lambda a: a.estado != 'fallecido' and a.especie_id.tipo_alimentacion == 'carnivoro'))
            else:
                record.cant_animales_carn = 0
    
    @api.depends('animales_ids', 'animales_ids.estado', 'animales_ids.especie_id')
    def _compute_cant_anim_omni(self):
        for record in self:
            if record.animales_ids:
                record.cant_animales_omni = len(record.animales_ids.filtered(lambda a: a.estado != 'fallecido' and a.especie_id.tipo_alimentacion == 'omnivoro'))
            else:
                record.cant_animales_omni = 0