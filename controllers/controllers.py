# -*- coding: utf-8 -*-
# from odoo import http


# class SampleGitModule(http.Controller):
#     @http.route('/sample_git_module/sample_git_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample_git_module/sample_git_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample_git_module.listing', {
#             'root': '/sample_git_module/sample_git_module',
#             'objects': http.request.env['sample_git_module.sample_git_module'].search([]),
#         })

#     @http.route('/sample_git_module/sample_git_module/objects/<model("sample_git_module.sample_git_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample_git_module.object', {
#             'object': obj
#         })
