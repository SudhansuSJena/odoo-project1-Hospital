{
  "name": "Hospital Management System",
  "author": "SUDHANSU SEKHAR JENA",
  "license": "LGPL-3",
  "version": "17.0.1.1",
  "depends": [
    "mail"  
  ],
  "data": [
      "security/ir.model.access.csv",
      "views/om_hospital_patient_wizard_views.xml",
      "views/om_hospital_patient_views.xml",
      "views/om_hospital_patient_readonly_views.xml",
      "views/om_hospital_doctor_views.xml",
      "views/om_hospital_doctor_readonly_views.xml",
      "views/om_hospital_menu.xml",

  ],
  "application": True, # Add this to make it appear in apps list
  "installable": True # Add this to make it installable
}
