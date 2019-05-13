# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Terricolas(models.Model):
 _name = 'dragonball_z.terricolas'
 _rec_name= 'nombre'
 nombre = fields.Char(string="Nombre",required=True)
 descripcion=fields.Char(string="Descripcion")
 edad=fields.Integer(string="Edad",required=True)
 fecha_nac=fields.Date(string="Fecha Nacimiento",required=True)
 hijos=fields.Many2one('dragonball_z.terricolas',
 'nombre'
 )
 #casado relacion uno a uno
 #hijos relaciono uno a muchos
class Namekiano(models.Model):
 _name = 'dragonball_z.namekiano'
 _rec_name= 'nombre_namekiano'
 nombre_namekiano = fields.Char(string="Nombre",required=True)
 descripcion_namekiano=fields.Char(string="Descripcion")
 edad_namekiano=fields.Integer(string="Edad",required=True)
 fecha_nac_namekiano=fields.Date(string="Fecha Nacimiento",required=True)
#  amigos_terricolas=fields.One2Many('dragonball_z.terricolas',
#  'nombre')
 #casado relacion uno a uno
 #hijos relaciono uno a muchos 