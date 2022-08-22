import datetime

from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date('Birthday')
    is_access = fields.Boolean(
        compute='_compute_access',
    )

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)

    def _compute_access(self):
        for rec in self:
            rec.is_access = rec.create_date > (datetime.datetime.now() - datetime.timedelta(days=30))
