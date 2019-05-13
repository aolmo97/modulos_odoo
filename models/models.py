# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Terricolas(models.Model):
    _name = 'dragon_ball_z.terricolas'

    _rec_name= 'nombre'
    nombre = fields.Char(string="Nombre",required=True)
    descripcion=fields.Char(string="Descripcion")
    edad=fields.Integer(string="Edad",required=True)
    fecha_nac=fields.Date(string="Fecha Nacimiento",required=True)
    #casado