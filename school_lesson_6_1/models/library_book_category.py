from odoo import fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Books Category'

    name = fields.Char(
        string='Book category'
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )
