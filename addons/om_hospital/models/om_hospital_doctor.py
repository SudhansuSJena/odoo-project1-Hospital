from odoo import models, fields, api, exceptions


class OmHospitalDoctor(models.Model):
    _name = "om_hospital.doctor"
    _description = "Doctor Master"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _ref_name = 'name' # This decides which field's value to be show in dropdown. By default its name field


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


    # name_get method is responsible for defining how a record is displayed when referred to in many-to-one or one-to-many relationships or drop-downs. This method customizes how the display name of a record is presented in views.
    def name_get(self):
        res = []
        for doctor in self:
            res.append((doctor.id, f"{doctor.name} - Experience: {doctor.experience} yrs"))

        return res
    
    def action_redirect_to_patient_tree(self):
        # return action dictionary to see patient tree view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Patients Tree View',
            'res_model': 'om_hospital.patient',
            'view_mode': 'tree,form',
            'target': 'current',
            'views': [(False, 'tree'), (False, 'form')]
        }
    
    def action_redirect_to_patient_kanban(self):
        # return action dictionary to see patient kanban
        return {
            'type': 'ir.actions.act_window',
            'name': 'Patients Kanban View' ,
            'res_model': 'om_hospital.patient',
            'view_mode': 'kanban,form',
            'target': 'new',
            'views': [(False, 'kanban'), (False, 'form')]
        }