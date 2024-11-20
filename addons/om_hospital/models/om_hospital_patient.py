from odoo import api, fields, models, exceptions

class OmHospitalPatient(models.Model):
    _name = "om_hospital.patient"
    _description = "Patient Master"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of birth", tracking=True)
    is_child = fields.Boolean(string="Is child ?", compute='_compute_is_child', tracking=True)
    age = fields.Integer(string="Age", required=True, tracking=True)

    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)


    
    @api.depends('age')
    def _compute_is_child(self):
        for patient in self:
            if patient.age >= 18:
                patient.is_child = False
            else:
                patient.is_child = True
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
        print("My vals: ")
        print(vals)
        if not vals.get('name'):
            raise exceptions.ValidationError("The name field is required.")
        
        record = super(OmHospitalPatient, self).create(vals)
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

    
    def write(self, vals):
        # FOr each record, store old values before the update
        print("My vals")

        for patient in self:
            is_update = super(OmHospitalPatient, self).write(vals)
        
        return is_update
            

        

    
    # unlink method: Handles deletion of records.
    # RULES:
    # 1. NO parameters: The method doesnot require any other parameter other than self, as it operates on the recordset(self).
    # 2. Return value: Must return a boolean(True/False) indicating whether the deletion was succesfully or not.
    # 3. call super(): Always call super() to perform actual deletion of record.
    # 4. Custom Logic: All validation to restrict deletion under certain condition or log deletion activity.

    
    def unlink(self):
        for patient in self:
            # Store the patient name for the message
            patient_name = patient.name
            
            # Perform the deletion
            is_unlink = super(OmHospitalPatient, self).unlink()
        return is_unlink


