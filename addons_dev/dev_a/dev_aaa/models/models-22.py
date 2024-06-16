# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dev_aaa(models.Model):
#     _name = 'dev_aaa.dev_aaa'
#     _description = 'dev_aaa.dev_aaa'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
