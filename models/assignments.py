from odoo import api, fields, models, _
from datetime import datetime, date
from odoo.exceptions import ValidationError, UserError


class Assignment(models.Model):
    _name = 'geneos.assignment'
    _inherit = 'account.analytic.line'
    _description = 'Modelo de asignaciones'

    employee_id = fields.Many2one(string='Associate', comodel_name='hr.employee', required=True)
    project_id = fields.Many2one(string='Project', comodel_name='project.project', required=True)
    name = fields.Char('Description', required=False)
    period = fields.Date(string='Period', required=True, default=date.today())
    period_name = fields.Char(string='Period', compute='_compute_period_name', store=True)
    unit_amount = fields.Float(string='Assigned hours')
    tag_ids = fields.Many2many('account.analytic.tag', 'assignment_tag_rel', 'assignment_id', 'tag_id', string='Tags', copy=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    average_hours = fields.Float(string='Average hours',compute='_compute_average_hours', store=True)
    DAYS_WEEK = 5
    AVERAGE_WEEKS = 4.35 

    date = fields.Date(compute='_compute_date')
    selectable_fields = ['employee_id','project_id', 'name', 'period', 'unit_amount','date', 'average_hours']

    exceeded = fields.Boolean(compute='_compute_exceeded', store=False)

    @api.model
    def fields_get(self, allfields=None, attributes=None):
       res = super(Assignment, self).fields_get(allfields, attributes=attributes)
       not_selectable_fields = set(res.keys()) - set(self.selectable_fields)
       for field in not_selectable_fields:
          res[field]['selectable'] = False # to hide in Add Custom filter view
          res[field]['sortable'] = False # to hide in group by view
          res[field]['exportable'] = False # to hide in export list
          res[field]['store'] = False # to hide in 'Select Columns' filter in tree views
       return res

    @api.depends('period')
    def _compute_period_name(self):
       for record in self:
          record.period_name = record.period.strftime('%h/%Y')

    @api.depends('period')
    def _compute_date(self):
       for record in self:
          record.date = record.period

    @api.constrains('employee_id', 'project_id', 'period_name')
    def _check_valid_assignment(self):
          for record in self:
             validate = self.env['geneos.assignment'].search([('project_id', '=', record.project_id.id),('employee_id', '=', record.employee_id.id)]).filtered(lambda x:x.period_name == record.period_name and x.id != record.id)
             if validate:
                raise ValidationError('Existing assignment for this project and associate in this month.')

    def _compute_average_hours(self):
        for record in self:
            record.average_hours = record.employee_id.resource_calendar_id.hours_per_day * record.AVERAGE_WEEKS * record.DAYS_WEEK

    def _compute_exceeded(self):
      for record in self:
         total_assignments = self.env['geneos.assignment'].search([('employee_id','=',record.employee_id.id),('period_name','=',record.period_name)])
         if sum(ta.unit_amount for ta in total_assignments) > record.average_hours:
            record.exceeded = True
         else:
            record.exceeded = False

    @api.onchange('unit_amount')
    def _check_total_assignments(self):
       for record in self:
         total_assignments = self.env['geneos.assignment'].search([('employee_id','=',record.employee_id.id),('period_name','=',record.period_name), ('project_id', '!=', record.project_id.id)])
         if record.unit_amount + sum(ta.unit_amount for ta in total_assignments) > record.average_hours:
            return {
               'warning': {
                  'title': _('Assignment exceeded!'),
                  'message': _('You have exceeded the hours to assign')}
               }