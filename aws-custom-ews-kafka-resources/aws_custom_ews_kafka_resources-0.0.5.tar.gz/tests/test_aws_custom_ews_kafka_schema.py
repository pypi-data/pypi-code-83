#!/usr/bin/env python

"""Tests for `aws_custom_ews_kafka_resources` package."""

import json
from pytest import raises
from troposphere import Template

from aws_custom_ews_kafka_resources import resource
from aws_custom_ews_kafka_resources import custom


def test_kafka_r_schema_value():
    """
    Function to test normal working of the
    :return:
    """
    template = Template()
    r_topic = resource.KafkaTopicSchema(
        "newtopicschema",
        RegistryUrl="http://registry.lan:8080",
        SerializeAttribute="key",
        CompatibilityMode="NONE",
        Type="AVRO",
        Definition={
            "name": "abcd",
            "namespace": "abcd",
            "fields": [{"type": "string", "name": "abcd"}],
        },
    )
    template.add_resource(r_topic)
    template.to_json()
    print(template.to_json())


def test_kafka_r_schema_value_string_def():
    """
    Function to test normal working of the
    :return:
    """
    template = Template()
    r_topic = resource.KafkaTopicSchema(
        "newtopicschema",
        RegistryUrl="http://registry.lan:8080",
        Type="AVRO",
        SerializeAttribute="value",
        CompatibilityMode="backward",
        Definition=json.dumps(
            {
                "name": "abcd",
                "namespace": "abcd",
                "fields": [{"type": "string", "name": "abcd"}],
            }
        ),
    )
    template.add_resource(r_topic)
    template.to_json()
    print(template.to_json())


def test_kafka_c_schema_value_string_def():
    """
    Function to test normal working of the
    :return:
    """
    template = Template()
    r_topic_schema = custom.KafkaTopicSchema(
        "newtopicschema",
        ServiceToken="somelambda",
        RegistryUrl="http://registry.lan:8080",
        CompatibilityMode="forward",
        Type="AVRO",
        SerializeAttribute="value",
        Definition=json.dumps(
            {
                "name": "abcd",
                "namespace": "abcd",
                "fields": [{"type": "string", "name": "abcd"}],
            }
        ),
    )
    template.add_resource(r_topic_schema)
    template.to_json()
    print(template.to_json())
