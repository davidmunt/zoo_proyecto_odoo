# -*- coding: utf-8 -*-

from datetime import date
from odoo.exceptions import UserError
from odoo import models, fields, api

class Animal(models.Model):
    _name = 'zoo.animal'

    raza = fields.Char(string="Raza", required=True)
    peso = fields.Float(string="Peso (kg)", required=True)
    altura = fields.Float(string="Altura (cm)", required=True)
    continente_origen = fields.Selection(
        [
            ('europa', 'Europa'),
            ('africa', 'Africa'),
            ('asia', 'Asia'),
            ('oceania', 'Oceania'),
            ('norteamerica', 'Norteamerica'),
            ('sudamerica', 'Sudamerica')
        ],
        copy=False,
        required=True,
        string="Continente de origen"
    )
    fecha_nac = fields.Date(required=True, store=True, string="Fecha de nacimiento")
    pais_origen = fields.Many2one('res.country', string='Pais')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    sexo = fields.Selection(
        [
            ('macho', 'Macho'),
            ('hembra', 'Hembra')
        ],
        copy=False,
        required=True,
        string="Sexo"
    )
    estado = fields.Selection(
        [
            ('disponible', 'Disponible'),
            ('enfermo', 'Enfermo'),
            ('fallecido', 'Fallecido')
        ],
        default='disponible',
        copy=False,
        required=True,
        string="Estado"
    )
    edad = fields.Integer(string="Edad", compute="_compute_edad", required=True)
    fecha_fall = fields.Date(string="Fecha de fallecimiento", compute="_compute_fall")
    foto = fields.Image(string="Foto")
    zoo_id = fields.Many2one("zoo.zoo", required=True, string="Zoo")
    
    @api.depends('fecha_nac')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nac:
                ahora = date.today()
                fecha_de_nacimiento = fields.Datetime.to_datetime(record.fecha_nac).date()
                total_edad = int((ahora - fecha_de_nacimiento).days / 365)
                record.edad = total_edad
            else:
                record.edad = 0
                
    @api.depends('estado')
    def _compute_fall(self):
        for record in self:
            if record.estado == 'fallecido':
                record.fecha_fall = date.today()
            else:
                record.fecha_fall = None
                
    @api.constrains('fecha_nac')
    def _verificar_fecha_nac(self):
        for record in self:
            ahora = date.today()
            if record.fecha_nac and record.fecha_nac > ahora:
                raise UserError('La fecha de nacimiento no puede estar en el futuro')
                
    @api.constrains('peso')
    def _verificar_peso(self):
        for record in self:
            if record.peso <= 0:
                raise UserError('El peso no puede ser igual a cero o un numero nagativo')
                
    @api.constrains('altura')
    def _verificar_altura(self):
        for record in self:
            if record.altura <= 0:
                raise UserError('La altura no puede ser igual a cero o un numero nagativo')
                
    def marcar_disponible(self):
        for record in self:
            if record.estado == 'disponible':
                raise UserError('El estado del animal ya esta en disponible')
            elif record.estado == 'fallecido':
                raise UserError('Este animal ha fallecido')
            record.estado = 'disponible'
    
    def marcar_enfermo(self):
        for record in self:
            if record.estado == 'enfermo':
                raise UserError('El estado del animal ya esta en enfermo')
            elif record.estado == 'fallecido':
                raise UserError('Este animal ha fallecido')
            record.estado = 'enfermo'
    
    def marcar_fallecido(self):
        for record in self:
            if record.estado == 'fallecido':
                raise UserError('El animal ya esta en estado Fallecido')
            record.estado = 'fallecido'