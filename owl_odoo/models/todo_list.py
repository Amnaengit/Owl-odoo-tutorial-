from odoo import api, fields, models


class OwlTodo(models.Model):
    _name = "owl.todo_list"
    _inherit = "mail.thread"
    _description = "owl Records"

    name = fields.Char(string='Name')
    completed = fields.Boolean()
    color = fields.Char()
