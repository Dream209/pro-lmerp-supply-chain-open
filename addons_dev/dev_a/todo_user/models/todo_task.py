# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ToDoTask(models.Model):
    _inherit = 'todo.task'
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help='What needs to be done?')