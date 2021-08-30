from odoo import fields, models, api, _


class AssetAssignment(models.Model):
    _name = 'cn.asset_assignment'
    _order = 'name'
    _description = 'Assignment'

    isActive = fields.Boolean('Assignment Active')
    assignmentDate = fields.Date('Assignment Date')
    assignmentDateEnd = fields.Date('Assignment Date End')
    assignmentDocument = fields.Binary('Assignment Document')

    assignment_rel_ids = fields.One2many(comodel_name='cn.asset_assignment_rel', inverse_name='assignment_id')

    @api.depends('isActive')
    def _change_active_status(self):
        if not self.isActive:
            self.assignmentDateEnd = fields.Date.today()
        for assignment_rel in self.assignment_rel_ids:
            assignment_rel.isActive = self.isActive
