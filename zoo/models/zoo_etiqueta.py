# -*- coding: utf-8 -*-

from datetime import date
from odoo.exceptions import UserError
from odoo import models, fields, api

class Etiqueta(models.Model):
    _name = 'zoo.etiqueta'

    name = fields.Char(string="Etiqueta", required=True)
    color = fields.Integer()
    descripcion = fields.Char(string="Descripcion", required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    zoo_id = fields.Many2many("zoo.zoo", string="Zoo")
    