# -*- coding: utf-8 -*-
# from odoo import http


# class Geneos-assignment(http.Controller):
#     @http.route('/geneos-assignment/geneos-assignment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geneos-assignment/geneos-assignment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geneos-assignment.listing', {
#             'root': '/geneos-assignment/geneos-assignment',
#             'objects': http.request.env['geneos-assignment.geneos-assignment'].search([]),
#         })

#     @http.route('/geneos-assignment/geneos-assignment/objects/<model("geneos-assignment.geneos-assignment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geneos-assignment.object', {
#             'object': obj
#         })
