from odoo import models, fields

class StockMarket(models.Model):
    _name = 'stock.market'
    _description = 'Stock Market'

    name = fields.Char('Stock Name')
    price = fields.Float('Stock Price')
    market_cap = fields.Float('Market Capitalization')
    volume = fields.Integer('Volume')
