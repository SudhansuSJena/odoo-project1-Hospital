from odoo import models, api, fields, exceptions


class OmHospitalPatientWizard(models.TransientModel):
    # The prefix om_hospital will clearly link the wizard to your existing module.
    _name="om_hospital.patient.wizard"
    _description=" Om Hospital Patient Delete Wizard"

    patient_name = fields.Char(string="Patient Name", required=True)


    def action_delete_patient(self):
        # Delete patient
        patient = self.env['om_hospital.patient'].search(domain=[("name", "=", self.patient_name)])
        if not patient:
            raise exceptions.UserError(f"No patient found of name: {self.patient_name}")
        
        patient.unlink()


    
    
    
