# -*- coding: utf-8 -*-

from odoo import models, fields

class Property(models.Model):
    _name = 'zoo.animal'

    raza = fields.Char(required=True)
    peso = fields.Float(string="Peso (KG)")
    altura = fields.Float(string="Altura (M)")
    continenteOrigen = fields.Char(required=True)
    fechaNac = fields.Date(required=True, store=True)
    paisOrigen = fields.Integer(required=True)
    sexo = fields.Selection(
        [
            ('Macho', 'Macho'),
            ('Hembra', 'Hembra')
        ],
        copy=False,
        string="Sexo"
    )