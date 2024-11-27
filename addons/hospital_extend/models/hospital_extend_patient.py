from odoo import fields, models, exceptions, api


class HospitalExtendPatient(models.Model):
    _inherit="om_hospital.patient"
    _description="Hospital Extent Patient"

    created_on = fields.Datetime(string="Created on", default=fields.Datetime.now)
    relationship_status = fields.Selection([("single", "Single"), ("married", "Married"), ("divorced", "Divorced")])
    
    # Created by field is Many2one type where one user can add many fields. ALl the ones will be in options. Here the comodel_name is "res.users"
    created_by=fields.Many2one(
        # res.users is a model which stores users information.
        # created_by field references res.users model using Many2one relationship
        comodel_name="res.users",
        string="Created by",
        default=lambda self: self.env.user,
        readonly=True
    )

    guardian=fields.Char(string="Guardian")

    # address details
    address=fields.Char(string="Address")
    city=fields.Char(string="City")
    state=fields.Char(string="State")

    # occupation details
    occupation=fields.Char(string="Occupation")
    company=fields.Char(string="Company")