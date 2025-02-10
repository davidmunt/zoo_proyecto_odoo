from datetime import date
from odoo.exceptions import UserError
from odoo import models, fields, api

class Horario(models.Model):
    _name = 'zoo.horario'
    _order = "orden_dia asc"

    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
        ('domingo', 'Domingo'),
    ], string="Dia de la Semana", required=True)
    apertura = fields.Float(string="Hora de Apertura", required=True, digits=(2, 2))
    cierre = fields.Float(string="Hora de Cierre", required=True, digits=(2, 2))
    orden_dia = fields.Integer(string="Orden del Dia", compute="_compute_orden_dia", store=True) 
    zoo_id = fields.Many2one('zoo.zoo', string="Zoo", required=True)
    
    @api.depends('dia_semana')
    def _compute_orden_dia(self):
        for record in self:
            match record.dia_semana:
                case "lunes":
                    record.orden_dia = 1
                case "martes":
                    record.orden_dia = 2
                case "miercoles":
                    record.orden_dia = 3
                case "jueves":
                    record.orden_dia = 4
                case "viernes":
                    record.orden_dia = 5
                case "sabado":
                    record.orden_dia = 6
                case "domingo":
                    record.orden_dia = 7
                case _:
                    record.orden_dia = 0

    @api.constrains('dia_semana', 'zoo_id')
    def _verificar_dia_unico(self):
        for record in self:
            existing_horarios = self.env['zoo.horario'].search([
                ('zoo_id', '=', record.zoo_id.id),
                ('dia_semana', '=', record.dia_semana),
                ('id', '!=', record.id)
            ])
            if existing_horarios:
                raise UserError('No puedes repetir el mismo dia en el horario de este zoo')
    
    @api.constrains('apertura', 'cierre')
    def _verificar_horas_validas(self):
        for record in self:
            if not (0.00 <= record.apertura < 24.00):  
                raise UserError('La hora de apertura tiene que estar entre 0.00 y 23.99')
            if not (0.00 < record.cierre <= 24.00):  
                raise UserError('La hora de cierre tiene que estar entre 0.01 y 24.00')
            if record.apertura >= record.cierre:
                raise UserError('La hora de apertura tiene que ser menor que la hora de cierre')
