# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/sigeesTaxi(http.Controller):
#     @http.route('//mnt/extra-addons/sigees_taxi//mnt/extra-addons/sigees_taxi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/sigees_taxi//mnt/extra-addons/sigees_taxi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/sigees_taxi.listing', {
#             'root': '//mnt/extra-addons/sigees_taxi//mnt/extra-addons/sigees_taxi',
#             'objects': http.request.env['/mnt/extra-addons/sigees_taxi./mnt/extra-addons/sigees_taxi'].search([]),
#         })

#     @http.route('//mnt/extra-addons/sigees_taxi//mnt/extra-addons/sigees_taxi/objects/<model("/mnt/extra-addons/sigees_taxi./mnt/extra-addons/sigees_taxi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/sigees_taxi.object', {
#             'object': obj
#         })

