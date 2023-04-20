from odoo import _,models, fields, api

class EmployerInfo(models.Model):
    _name = "employer.employer"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    phone_number = fields.Integer(string="phone_number")
    address = fields.Char(string="Address")
    education = fields.Char(string="education")
    employer_id = fields.Char(string="Employer_id")
    image = fields.Image(string='Image')
    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active', Tracking='True')
    gender = fields.Selection(related='customer_ids.gender', string="Gender")
    customer_ids = fields.Many2many('customer.customer', string="Customer")







