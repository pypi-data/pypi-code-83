""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields
from ucloud.services.usms.schemas import models


""" USMS API Schema
"""


"""
API: CreateUSMSSignature

调用接口CreateUSMSSignature申请短信签名
"""


class CreateUSMSSignatureRequestSchema(schema.RequestSchema):
    """CreateUSMSSignature - 调用接口CreateUSMSSignature申请短信签名"""

    fields = {
        "CertificateType": fields.Int(required=True, dump_to="CertificateType"),
        "Description": fields.Str(required=True, dump_to="Description"),
        "File": fields.Str(required=True, dump_to="File"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ProxyFile": fields.Str(required=False, dump_to="ProxyFile"),
        "SigContent": fields.Str(required=True, dump_to="SigContent"),
        "SigPurpose": fields.Int(required=True, dump_to="SigPurpose"),
        "SigType": fields.Int(required=True, dump_to="SigType"),
    }


class CreateUSMSSignatureResponseSchema(schema.ResponseSchema):
    """CreateUSMSSignature - 调用接口CreateUSMSSignature申请短信签名"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "SigContent": fields.Str(required=False, load_from="SigContent"),
        "SigId": fields.Str(required=False, load_from="SigId"),
    }


"""
API: CreateUSMSTemplate

调用接口CreateUSMSTemplate申请短信模板
"""


class CreateUSMSTemplateRequestSchema(schema.RequestSchema):
    """CreateUSMSTemplate - 调用接口CreateUSMSTemplate申请短信模板"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Purpose": fields.Int(required=True, dump_to="Purpose"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Template": fields.Str(required=True, dump_to="Template"),
        "TemplateName": fields.Str(required=True, dump_to="TemplateName"),
        "UnsubscribeInfo": fields.Str(
            required=False, dump_to="UnsubscribeInfo"
        ),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class CreateUSMSTemplateResponseSchema(schema.ResponseSchema):
    """CreateUSMSTemplate - 调用接口CreateUSMSTemplate申请短信模板"""

    fields = {
        "Message": fields.Str(required=True, load_from="Message"),
        "TemplateId": fields.Str(required=True, load_from="TemplateId"),
    }


"""
API: DeleteUSMSSignature

调用接口DeleteUSMSSignature删除短信签名
"""


class DeleteUSMSSignatureRequestSchema(schema.RequestSchema):
    """DeleteUSMSSignature - 调用接口DeleteUSMSSignature删除短信签名"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "SigIds": fields.List(fields.Str()),
    }


class DeleteUSMSSignatureResponseSchema(schema.ResponseSchema):
    """DeleteUSMSSignature - 调用接口DeleteUSMSSignature删除短信签名"""

    fields = {"Message": fields.Str(required=True, load_from="Message")}


"""
API: DeleteUSMSTemplate

调用接口DeleteUSMSTemplate删除短信模板
"""


class DeleteUSMSTemplateRequestSchema(schema.RequestSchema):
    """DeleteUSMSTemplate - 调用接口DeleteUSMSTemplate删除短信模板"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "TemplateIds": fields.List(fields.Str()),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class DeleteUSMSTemplateResponseSchema(schema.ResponseSchema):
    """DeleteUSMSTemplate - 调用接口DeleteUSMSTemplate删除短信模板"""

    fields = {"Message": fields.Str(required=True, load_from="Message")}


"""
API: GetUSMSSendReceipt

获取短信发送回执信息。下游服务提供商回执信息返回会有一定延时，建议发送完短信以后，5-10分钟后再调用该接口拉取回执信息。若超过12小时未返回，则请联系技术支持确认原因
"""


class GetUSMSSendReceiptRequestSchema(schema.RequestSchema):
    """GetUSMSSendReceipt - 获取短信发送回执信息。下游服务提供商回执信息返回会有一定延时，建议发送完短信以后，5-10分钟后再调用该接口拉取回执信息。若超过12小时未返回，则请联系技术支持确认原因"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "SessionNoSet": fields.List(fields.Str()),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class GetUSMSSendReceiptResponseSchema(schema.ResponseSchema):
    """GetUSMSSendReceipt - 获取短信发送回执信息。下游服务提供商回执信息返回会有一定延时，建议发送完短信以后，5-10分钟后再调用该接口拉取回执信息。若超过12小时未返回，则请联系技术支持确认原因"""

    fields = {
        "Data": fields.List(
            models.ReceiptPerSessionSchema(), required=True, load_from="Data"
        ),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: QueryUSMSSignature

调用接口QueryUSMSSignature查询短信签名申请状态
"""


class QueryUSMSSignatureRequestSchema(schema.RequestSchema):
    """QueryUSMSSignature - 调用接口QueryUSMSSignature查询短信签名申请状态"""

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "SigContent": fields.Str(required=False, dump_to="SigContent"),
        "SigId": fields.Str(required=False, dump_to="SigId"),
    }


class QueryUSMSSignatureResponseSchema(schema.ResponseSchema):
    """QueryUSMSSignature - 调用接口QueryUSMSSignature查询短信签名申请状态"""

    fields = {
        "Data": models.OutSignatureSchema(),
        "Message": fields.Str(required=True, load_from="Message"),
    }


"""
API: QueryUSMSTemplate

调用接口QueryUSMSTemplate查询短信模板申请状态
"""


class QueryUSMSTemplateRequestSchema(schema.RequestSchema):
    """QueryUSMSTemplate - 调用接口QueryUSMSTemplate查询短信模板申请状态"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "TemplateId": fields.Str(required=True, dump_to="TemplateId"),
    }


class QueryUSMSTemplateResponseSchema(schema.ResponseSchema):
    """QueryUSMSTemplate - 调用接口QueryUSMSTemplate查询短信模板申请状态"""

    fields = {
        "Data": models.OutTemplateSchema(),
        "Message": fields.Str(required=False, load_from="Message"),
    }


"""
API: SendUSMSMessage

发送短信息。短信字数超过70个后，按照每66个进行切割(因为要加上1/3), 2/3)等字样，占用4个字长)。短信最大长度不能超过600个字。每个汉字、数字、字母、字符都按一个字计
"""


class SendUSMSMessageRequestSchema(schema.RequestSchema):
    """SendUSMSMessage - 发送短信息。短信字数超过70个后，按照每66个进行切割(因为要加上1/3), 2/3)等字样，占用4个字长)。短信最大长度不能超过600个字。每个汉字、数字、字母、字符都按一个字计"""

    fields = {
        "PhoneNumbers": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "SigContent": fields.Str(required=False, dump_to="SigContent"),
        "TemplateId": fields.Str(required=True, dump_to="TemplateId"),
        "TemplateParams": fields.List(fields.Str()),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class SendUSMSMessageResponseSchema(schema.ResponseSchema):
    """SendUSMSMessage - 发送短信息。短信字数超过70个后，按照每66个进行切割(因为要加上1/3), 2/3)等字样，占用4个字长)。短信最大长度不能超过600个字。每个汉字、数字、字母、字符都按一个字计"""

    fields = {
        "Action": fields.Str(required=True, load_from="Action"),
        "Message": fields.Str(required=True, load_from="Message"),
        "RetCode": fields.Int(required=True, load_from="RetCode"),
        "SessionNo": fields.Str(required=False, load_from="SessionNo"),
    }


"""
API: UpdateUSMSSignature

调用接口UpdateUSMSSignature修改未通过审核的短信签名，并重新提交审核
"""


class UpdateUSMSSignatureRequestSchema(schema.RequestSchema):
    """UpdateUSMSSignature - 调用接口UpdateUSMSSignature修改未通过审核的短信签名，并重新提交审核"""

    fields = {
        "CertificateType": fields.Int(
            required=False, dump_to="CertificateType"
        ),
        "File": fields.Str(required=True, dump_to="File"),
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ProxyFile": fields.Str(required=False, dump_to="ProxyFile"),
        "SigContent": fields.Str(required=True, dump_to="SigContent"),
        "SigId": fields.Str(required=True, dump_to="SigId"),
        "SigPurpose": fields.Int(required=True, dump_to="SigPurpose"),
        "SigType": fields.Int(required=True, dump_to="SigType"),
    }


class UpdateUSMSSignatureResponseSchema(schema.ResponseSchema):
    """UpdateUSMSSignature - 调用接口UpdateUSMSSignature修改未通过审核的短信签名，并重新提交审核"""

    fields = {"Message": fields.Str(required=True, load_from="Message")}


"""
API: UpdateUSMSTemplate

调用接口UpdateUSMSTemplate修改未通过审核的短信模板，并重新提交审核
"""


class UpdateUSMSTemplateRequestSchema(schema.RequestSchema):
    """UpdateUSMSTemplate - 调用接口UpdateUSMSTemplate修改未通过审核的短信模板，并重新提交审核"""

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "Region": fields.Str(required=False, dump_to="Region"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Template": fields.Str(required=True, dump_to="Template"),
        "TemplateId": fields.Str(required=True, dump_to="TemplateId"),
        "TemplateName": fields.Str(required=False, dump_to="TemplateName"),
        "UnsubscribeInfo": fields.Str(
            required=False, dump_to="UnsubscribeInfo"
        ),
        "Zone": fields.Str(required=False, dump_to="Zone"),
    }


class UpdateUSMSTemplateResponseSchema(schema.ResponseSchema):
    """UpdateUSMSTemplate - 调用接口UpdateUSMSTemplate修改未通过审核的短信模板，并重新提交审核"""

    fields = {"Message": fields.Str(required=True, load_from="Message")}
