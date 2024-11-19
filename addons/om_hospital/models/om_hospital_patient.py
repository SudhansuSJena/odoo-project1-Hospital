from odoo import api, fields, models

class OmHospitalPatient(models.Model):
    _name = "om_hospital.patient"
    _description = "Patient Master"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of birth", tracking=True)

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)