from odoo import models, fields, api, exceptions


class OmHospitalDoctor(models.Model):
    _name = "om_hospital.doctor"
    _description = "Doctor Master"
    _inherit = ["mail.thread"]


    name = fields.Char(string="Name", required=True, tracking=True)
    experience = fields.Integer(string="Experience", compute="_compute_experience", tracking=True, required=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], tracking=True)
    experience_level = fields.Selection([("beginner", "Beginner"), ("intermediate", "Intermediate"), ("experienced", "Experienced"), ("master", "Master")], compute="_compute_experience_level",required=True, tracking=True)


    @api.depends('age')
    def _compute_experience_level(self):
        for doctor in self:
            if(doctor.age >= 25 and doctor.age < 30):
                doctor.experience_level = "beginner"
            elif(doctor.age >= 30 and doctor.age < 40):
                doctor.experience_level = "intermediate"
            elif(doctor.age >= 40 and doctor.age < 50):
                doctor.experience_level = "experienced"
            else:
                doctor.experience_level = "master"

    @api.constrains('age')
    def _check_age(self):
        for doctor in self:
            if(doctor.age < 25):
                raise exceptions.UserError("Doctor's age must be 25 or greater than 25.")
            
    @api.depends('age')
    def _compute_experience(self):
        for doctor in self:
            doctor.experience = doctor.age - 25
