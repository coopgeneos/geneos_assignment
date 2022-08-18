from unicodedata import category
from odoo import api, models, fields

#clase para la etiqueda de un proyecto
class ProjectTags(models.Model):
    """ Etiquetas del proyecto """
    _name = "project.tag"
    _description = "Etiquetas de proyecto"

    name = fields.Char('Nombre etiqueta', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "El nombre de esa etiqueta ya existe!"),
    ]
