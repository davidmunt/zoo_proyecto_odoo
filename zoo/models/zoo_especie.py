# -*- coding: utf-8 -*-

from odoo import models, fields

class Especie(models.Model):
    _name = 'zoo.especie'

    familia = fields.Char(required=True, String="Familia")
    nom_cientifico = fields.Char(required=True, String="Nombre cientifico")
    nom_vulgar = fields.Char(required=True, String="Nombre vulgar")
    peligro_extincion = fields.Boolean(required=True, String="Pelogro de extinción")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    nivel_peligro = fields.Selection(
        [
            ('alto', 'Alto'),
            ('medio', 'Medio'),
            ('bajo', 'Bajo'),
            ('nulo', 'Nulo')
        ],
        copy=False,
        string="Nivel de peligro"
    )
    tipo_alimentacion = fields.Selection(
        [
            ('carnivoro', 'Carnívoro'),
            ('hervivoro', 'Hervívoro'),
            ('omnivoro', 'Omnívoro')
        ],
        copy=False,
        string="Tipo de alimentacion"
    )