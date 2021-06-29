from odoo import api, models, fields

class ReproProject(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    is_repro = fields.Boolean(string='Reproductive', default=False)    