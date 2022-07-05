from odoo import api, fields, models

class AMDLModel(models.Model):
    _name = "amdl.model"
    _description = "AMDL Model"

    name = fields.Char(required=True)










