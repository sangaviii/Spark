from odoo import _,models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, date


class Customer(models.Model):
    _name = "customer.customer"

    @api.model
    def _get_default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    @api.model
    def _get_default_user_name(self):
        return self.env.user.name

    name = fields.Char(string="Name")
    first_name = fields.Char(string="first_Name")
    last_name = fields.Char(string="last_Name")
    age = fields.Integer(string="Age")
    phone_no = fields.Char(string="Phone_no")
    image = fields.Image(string="Image")
    payment = fields.Selection([
        ('gold', 'Gold'),
        ('silver', 'Silver')], 'payment')
    bill = fields.Float(string="Bill")
    gender = fields.Selection([('male', 'Male'), ('female', "Female")], 'Gender')
    address = fields.Char(string="Address")
    status = fields.Selection([
        ('on duty', 'On duty'),
        ('of duty', 'Of duty')],
        'Status',
        )
    # user_id = fields.Integer(string="User_Id")

    color = fields.Integer(string="color")
    due_start_date = fields.Datetime(string="due_start_Date")
    due_end_date = fields.Datetime(string="due_end_Date")
    dob = fields.Date(string="DOB")
    user_id = fields.Many2one('res.users', string='User', default=_get_default_user)
    user_name = fields.Char('use Name', default=_get_default_user_name)
    customer_code = fields.Char(string="Customer_code")
    total = fields.Float('Total', compute="_compute_bill_total", store=True)
    bike_name = fields.Char(String="Bike_name")
    work_status = fields.Selection([
        ('on duty', 'On duty'),
        ('of duty', 'Of duty')],
        'work_status',
        default='on duty')

    @api.onchange('first_name', 'last_name')
    def onchange_name(self):
        if self.first_name and self.last_name:
            self.name = '%s %s' % (self.first_name, self.last_name)

    _sql_constraints = [
        ('customer_code_uniq', 'unique (customer_code)', 'The Customer Code must be unique !')
    ]


    @api.constrains('age')
    def _constraints_age(self):
        for record in self:
            if record.age < 18:
                raise UserError(_("Customer Age must be above 18!"))

    @api.onchange('dob')
    def _onchange_dob(self):
        if self.dob:
            current_date = date.today()
            current_year = current_date.year
            date_of_birth_year = self.dob.year
            self.age = current_year - date_of_birth_year

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, '%s (%s)' % (record.age, record.name)))
        return res

    @api.model
    def create(self, vals):
        print('sssss', vals)
        vals['bike_name'] = 'r15'
        return super(Customer, self).create(vals)


    def set_work_status(self, vals):
        if vals.get('work_status') == 'on duty':
            vals['status'] = 'on duty'
        elif vals.get('work_status') == 'of duty':
            vals['status'] = 'of duty'
        return vals

    def write(self, vals):
        vals = self.set_work_status(vals)
        res = super(Customer, self).write(vals)
        return res








