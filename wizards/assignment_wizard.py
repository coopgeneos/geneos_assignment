from odoo import api, fields, models
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class ModuleName(models.TransientModel):
    _name = 'geneos.assignment_wizard'
    _description = 'Wizard de generación de asignaciones'

    employee_id = fields.Many2one(string='Associate', comodel_name='hr.employee', required=True)
    project_id = fields.Many2one(string='Project', comodel_name='project.project', required=True)
    date_init = fields.Date(string='Date To', required=True)
    date_end = fields.Date(string='Date From', required=True)
    hours = fields.Float(string='Hours to assign', default=0)



    def generate_assignments(self):
        months = 12 * (self.date_end.year - self.date_init.year) + self.date_end.month - self.date_init.month
        for i in range(0, months):
            period_date = (self.date_init + relativedelta(months= i))
            vals  = {
                'employee_id': self.employee_id.id,
                'project_id': self.project_id.id,
                'period': period_date,
                'unit_amount': self.hours
            }
            self.env['geneos.assignment'].create(vals)

    @api.constrains('date_end')
    def _constrains_date_end(self):
        for record in self:
            if record.date_init > record.date_end:
                raise ValidationError("Date To must be upper than Date From")