from marshmallow import Schema, fields

from project.extensions import ma


class TranslateSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    uid = fields.String(required=False)
    original_text = fields.String(required=True)
    translated_text = fields.String(required=False)
    order_number = fields.Integer(required=False)
    status = fields.String(required=False)
