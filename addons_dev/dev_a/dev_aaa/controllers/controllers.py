# -*- coding: utf-8 -*-
# from odoo import http


# class DevAaa(http.Controller):
#     @http.route('/dev_aaa/dev_aaa', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_aaa/dev_aaa/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_aaa.listing', {
#             'root': '/dev_aaa/dev_aaa',
#             'objects': http.request.env['dev_aaa.dev_aaa'].search([]),
#         })

#     @http.route('/dev_aaa/dev_aaa/objects/<model("dev_aaa.dev_aaa"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_aaa.object', {
#             'object': obj
#         })
