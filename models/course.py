from openerp import models, fields


class ModelCourse(models.Model):

    _name = "model.course"
    _description = "Model Course"

    name = fields.Char(String="Char", required=True)
    description = fields.Text(String="Text")
    responsible_id = fields.Many2one('res.users')
    session_id = fields.One2many('model.session', 'id')


class Session(models.Model):

    _name = "model.session"
    _description = "Model Session"

    name = fields.Char(String="Name", required=True)
    start_date = fields.Date("Date", required=True)
    duration = fields.Integer("Duration", required=True)
    instructor_id = fields.Many2one('res.partner')
    course_id = fields.Many2one('model.course')
    attendee_id = fields.One2many('model.attendee', 'id')


class Attendee(models.Model):

    _name = "model.attendee"
    _description = "Model Attendee"

    name = fields.Char(String="Char")
    partner_id = fields.Many2one('res.partner')
    session_id = fields.Many2one('model.session')


class Partner(models.Model):

    """
        Delegation inheritance
            - Multiple inheritance is possible
            - New Class Ignored by existing views
            - Stored in different tables
            - 'new' instances contain embedded 'Model A' instance with
            synchronized values
    """
    _inherit = "res.partner"

    is_instructor = fields.Boolean(string="Is instructor?")
    session_id = fields.Many2one('model.session')
