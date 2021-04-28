""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class ParamSchema(schema.ResponseSchema):
    """Param - 工作流参数"""

    fields = {
        "Name": fields.Str(required=False, load_from="Name"),
        "Type": fields.Str(required=False, load_from="Type"),
        "Value": fields.Str(required=False, load_from="Value"),
    }


class ActivityTemplateSchema(schema.ResponseSchema):
    """ActivityTemplate - 工作流的Activity定义"""

    fields = {
        "Input": fields.Str(),
        "Name": fields.Str(required=False, load_from="Name"),
        "Next": fields.Str(required=False, load_from="Next"),
        "Output": fields.List(fields.Str()),
        "RetryTimes": fields.Str(required=False, load_from="RetryTimes"),
        "Timeout": fields.Str(required=False, load_from="Timeout"),
        "Type": fields.Str(required=False, load_from="Type"),
    }


class WorkflowTemplateSchema(schema.ResponseSchema):
    """WorkflowTemplate - Workflow对象定义"""

    fields = {
        "Activites": fields.List(ActivityTemplateSchema()),
        "Input": fields.List(ParamSchema()),
        "Output": fields.List(ParamSchema()),
    }
