from odoo import _,models, fields,api


class Manager(models.Model):
    _name = 'manager.manager'

    first_name = fields.Char(string="First_Name")
    last_name = fields.Char(string="Last_Name")
    name = fields.Char(string='Name')
    image = fields.Image(string='Image')
    dob = fields.Date(string="DOB")
    age = fields.Integer(string="Age")
    phone_number = fields.Integer(string="phone_number")
    email = fields.Char(string="email")
    address = fields.Char(string="Address")
    education = fields.Char(string="education")
    gender = fields.Selection([('male', 'Male'), ('female', "Female")], 'Gender')
    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active')
