from odoo import _, fields, models, api


class Bike_productInfo(models.Model):
    _name = "bike.bike"
    _description = "bike_products Profile"

    bike_name = fields.Char(string="Name", required=True)
    customer_id = fields.Many2one('customer.customer', string="Customer")
    email = fields.Char(string="email")
    image = fields.Image(string="Image")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if 'bike_name' not in default:
            default['bike_name'] = _("%s (copy)") % self.bike_name
        return super(Bike_productInfo, self).copy(default=default)


    #
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         res.append((record.id, '%s (%s)' % (record.bill, record.name)))
    #     return res

