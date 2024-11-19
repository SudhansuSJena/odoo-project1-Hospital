from odoo import api, fields, models, exceptions

class OmHospitalPatient(models.Model):
    _name = "om_hospital.patient"
    _description = "Patient Master"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of birth", tracking=True)

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)

    # Create method: Handle creation of new record.
    # RULES
    # create method takes 2 arguments self and vals
    # 1. Accept vals as parameter:
    # - vals is a dictionary of field values to be inserted into the database
    # - example: {'name': 'Ram', 'gender': 'male'}
    # 2. Return value:
    # - Must return a recordset containing the newly created record.
    # 3. call super():
    # - always call super() to perform the actual creation of the record.
    # 4. custom logic:
    # - Add validation, set default values or trigger additional logic.

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            raise exceptions.ValidationError("The name field is required.")
        
        record = super(OmHospitalPatient, self).create(vals)
        record.message_post(body=f"Patient {record.name} has been created.")
        print("My record: ")
        print(record)
        return record # recordset
    
    # WRITE METHOD: Handles updating the existing records.
    # RULES:
    # 1. Accepts vals as a parameter:
    # - vals is a dictionary containing fields to be updated and their values.
    # - example: {'name': 'Rahul Jena'}
    # 2. Return value: Must return a boolean(True/False) indicating whether the operation was successful or not.
    # 3. Call super(): Always call super() to perform the actual update of the record.
    # 4. Custom logic: Add validation, set default values or trigger additional logic.

    @api.model
    def write(self, vals):
        for patient in self:

            # Log updation in chatter.
            old_name = patient.name
            new_name = vals.get('name')
        
            is_update = super(OmHospitalPatient, self).write(vals)

            if(is_update):
                patient.message_post(body=f"Old Name: {old_name} updated to New Name: {new_name}")
            else:
                patient.message_post(body=f"Failed to update name.")
        
        return is_update
            

        

    
    # unlink method: Handles deletion of records.
    # RULES:
    # 1. NO parameters: The method doesnot require any paramaeter, as it operates on the recordset(self).
    # 2. Return value: Must return a boolean(True/False) indicating whether the deletion was succesfully or not.
    # 3. call super(): Always call super() to perform actual deletion of record.
    # 4. Custom Logic: All validation to restrict deletion under certain condition or log deletion activity.

    @api.model
    def unlink(self):
        for patient in self:

            # Log deletion in chatter
            patient_name = patient.name
            is_unlink = super(OmHospitalPatient, self).unlink()
            if(is_unlink):
                patient.message_post(body=f"Patient '{patient_name}' record deleted successfully.")
            else:
                patient.message_post(body=f"Failed to delete patient '{patient_name}'.")

        return is_unlink

