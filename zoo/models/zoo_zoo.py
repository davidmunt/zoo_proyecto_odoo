# -*- coding: utf-8 -*-

from odoo import models, fields

class Zoo(models.Model):
    _name = 'zoo.zoo'

    nombre = fields.Char(required=True, String="Nombre")
    ciudad = fields.Integer(required=True, String="Ciudad") #de momento no hago relacion con nada
    pais = fields.Integer(required=True, String="Pais") #de momento no hago la relacion con res_country
    superficie = fields.Float(required=True, default=0, String="Superficie (M)")