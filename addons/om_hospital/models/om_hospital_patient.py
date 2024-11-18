from odoo import api, fields, models

class OmHospitalPatient(models.Model):
    _name = "om_hospital.patient"
    _description = "Patient Master"

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string="Date of birth")

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")