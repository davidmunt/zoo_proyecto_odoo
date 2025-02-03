# -*- coding: utf-8 -*-

from odoo import models, fields

class Especie(models.Model):
    _name = 'zoo.especie'

    name = fields.Char(required=True, String="Nombre vulgar")
    nom_cientifico = fields.Char(required=True, String="Nombre cientifico")
    familia = fields.Char(required=True, String="Familia")
    peligro_extincion = fields.Boolean(required=True, String="Pelogro de extinción")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    animales_ids = fields.One2many("zoo.animal", "especie_id", string="Animales")
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