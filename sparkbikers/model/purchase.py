from odoo import fields, models, api


class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.price_total', 'price')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                line._compute_amount()
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            currency = order.currency_id or order.partner_id.property_purchase_currency_id or self.env.company.currency_id
            order.update({
                'amount_untaxed': currency.round(amount_untaxed),
                'amount_tax': currency.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
                'total_price': amount_untaxed + amount_tax + order.price

            })



    price = fields.Integer(string='Price')
    total_price = fields.Monetary(comput='_amount_all', string='Total Amount')


class Purchaseline(models.Model):
    _inherit = 'purchase.order.line'

    offer_code = fields.Integer(string='Offer_code')
    # bike = fields.Many2one('bike.bike', string='Bike')
