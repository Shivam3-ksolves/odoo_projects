from odoo import models, fields

class NewsArticle(models.Model):
    _name = 'news.article'  # Unique identifier for the model
    _description = 'News Article'

    title = fields.Char(string="Title", required=True)  # A required text field
    content = fields.Text(string="Content")  # A larger text field
    published_date = fields.Date(string="Published Date")  # Date field
