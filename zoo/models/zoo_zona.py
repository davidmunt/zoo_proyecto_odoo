from odoo import models, fields, api

class Zona(models.Model):
    _name = 'zoo.zona'

    name = fields.Char(string="Nombre de la Zona", required=True)
    descripcion = fields.Text(string="Descripcion", help="Descripcion de la zona")
    animal_ids = fields.One2many('zoo.animal', 'zona_id', string="Animales en esta zona")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
