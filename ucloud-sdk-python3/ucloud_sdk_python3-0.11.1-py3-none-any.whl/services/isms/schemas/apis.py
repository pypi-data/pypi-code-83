""" Code is generated by ucloud-model, DO NOT EDIT IT. """


from ucloud.core.typesystem import schema, fields
from ucloud.services.isms.schemas import models

""" ISMS API Schema
"""


"""
API: GetISMSSendReceipt

获取视频短信发送记录的状态回执
"""


class GetISMSSendReceiptRequestSchema(schema.RequestSchema):
    """GetISMSSendReceipt - 获取视频短信发送记录的状态回执"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "TaskIdSet": fields.List(fields.Str()),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class GetISMSSendReceiptResponseSchema(schema.ResponseSchema):
    """GetISMSSendReceipt - 获取视频短信发送记录的状态回执"""

    fields = {
        "Data": fields.List(
            models.ReceiptPerTaskSchema(), required=False, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
        "ReqUuid": fields.Str(required=True, load_from="ReqUuid"),
    }


"""
API: SendISMSMessage

发送视频短信
"""


class SendISMSMessageRequestSchema(schema.RequestSchema):
    """SendISMSMessage - 发送视频短信"""

    fields = {
        "PhoneSet": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "TemplateId": fields.Str(required=True, dump_to="TemplateId"),
        "Zone": fields.Str(required=True, dump_to="Zone"),
    }


class SendISMSMessageResponseSchema(schema.ResponseSchema):
    """SendISMSMessage - 发送视频短信"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "ReqUuid": fields.Str(required=True, load_from="ReqUuid"),
        "TaskId": fields.Str(required=True, load_from="TaskId"),
    }
