from openerp import models, fields

class ModelCourse(models.Model):

    _name = "model.course"
    _description = "Model Course"

    name = fields.Char(String="Char", required=True)
    description = fields.Char(String="Char")