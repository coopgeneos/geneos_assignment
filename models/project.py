from unicodedata import category
from odoo import api, models, fields

class ReproProject(models.Model):
    _inherit = 'project.project'

    is_repro = fields.Boolean(string='Reproductive', default=False)

    #Campo etiqueta en el proyecto
    tags_id = fields.Many2many(string='Etiqueta de proyecto', comodel_name='project.tag')  