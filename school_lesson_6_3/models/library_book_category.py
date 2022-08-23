from odoo import models, fields


class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'
    #The class inherit the Book Category model from the module school_lesson_6_1

    def action_category_books(self):
        """Determine options for opening the tree when the button for filtering books by category is clicked.

        :return dictionary:
        """
        return {
            'name': 'Category books',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'library.book',
            'context': {'search_default_category_id': self.ids[0]}
        }
