# -*- coding: utf-8 -*-
from odoo import http

# class DragonBallZ(http.Controller):
#     @http.route('/dragon_ball_z/dragon_ball_z/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dragon_ball_z/dragon_ball_z/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dragon_ball_z.listing', {
#             'root': '/dragon_ball_z/dragon_ball_z',
#             'objects': http.request.env['dragon_ball_z.dragon_ball_z'].search([]),
#         })

#     @http.route('/dragon_ball_z/dragon_ball_z/objects/<model("dragon_ball_z.dragon_ball_z"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dragon_ball_z.object', {
#             'object': obj
#         })