# -*- coding: utf-8 -*-

from odoo import models, fields

class Property(models.Model):
    _name = 'zoo.especie'

    familia = fields.Char(required=True, String="Familia")
    nomCientifico = fields.Date(required=True, String="Nombre cientifico")
    nomVulgar = fields.Date(required=True, String="Nombre vulgar")
    peligroso = fields.Boolean(required=True)
    peligro = fields.Selection(
        [
            ('Alto', 'Alto'),
            ('Medio', 'Medio'),
            ('Bajo', 'Bajo')
        ],
        copy=False,
        string="Nivel de Peligro"
    )
    tipo_alimentacion = fields.Selection(
        [
            ('Carnivoro', 'Carnívoro'),
            ('Hervivoro', 'Hervívoro'),
            ('Omnivoro', 'Omnívoro')
        ],
        copy=False,
        string="Tipo de Alimentacion"
    )