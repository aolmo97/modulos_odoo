# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Terricolas(models.Model):
 _name = 'dragonball_z.terricolas'
 _rec_name= 'nombre'
 nombre = fields.Char(string="Nombre",required=True)
 descripcion=fields.Char(string="Descripcion")
 edad=fields.Integer(string="Edad",required=True)
 fecha_nac=fields.Date(string="Fecha Nacimiento",required=True)
 hijos=fields.Many2many('dragonball_z.terricolas', 'nombre')
 #casado relacion uno a uno
 #casado=fields.
 #hijos relaciono uno a muchos
 #hijos=fields.One2many('dragonball_z.terricolas', 'nombre')
class Namekiano(models.Model):
 _name = 'dragonball_z.namekiano'
 _rec_name= 'nombre_namekiano'
 nombre_namekiano = fields.Char(string="Nombre",required=True)
 descripcion=fields.Char(string="Descripcion")
 edad=fields.Integer(string="Edad",required=True)
 fecha_nac=fields.Date(string="Fecha Nacimiento",required=True)
 #casado relacion uno a uno
 #hijos relaciono uno a muchos 