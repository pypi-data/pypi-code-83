# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/entailment/v1/entailment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arg_services.base.v1 import base_pb2 as arg__services_dot_base_dot_v1_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arg_services/entailment/v1/entailment.proto',
  package='arg_services.entailment.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+arg_services/entailment/v1/entailment.proto\x12\x1a\x61rg_services.entailment.v1\x1a\x1f\x61rg_services/base/v1/base.proto\"e\n\x11\x45ntailmentRequest\x12\x30\n\x08language\x18\x01 \x01(\x0e\x32\x1e.arg_services.base.v1.Language\x12\x0f\n\x07premise\x18\x02 \x01(\t\x12\r\n\x05\x63laim\x18\x03 \x01(\t\"\x85\x01\n\x12\x45ntailmentResponse\x12:\n\nprediction\x18\x01 \x01(\x0e\x32&.arg_services.entailment.v1.Prediction\x12\x33\n\x07\x64\x65tails\x18\x02 \x03(\x0b\x32\".arg_services.entailment.v1.Detail\"Y\n\x06\x44\x65tail\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12:\n\nprediction\x18\x02 \x01(\x0e\x32&.arg_services.entailment.v1.Prediction*y\n\nPrediction\x12\x1a\n\x16PREDICTION_UNSPECIFIED\x10\x00\x12\x19\n\x15PREDICTION_ENTAILMENT\x10\x01\x12\x1c\n\x18PREDICTION_CONTRADICTION\x10\x02\x12\x16\n\x12PREDICTION_NEUTRAL\x10\x03\x32\x80\x01\n\x11\x45ntailmentService\x12k\n\nEntailment\x12-.arg_services.entailment.v1.EntailmentRequest\x1a..arg_services.entailment.v1.EntailmentResponseb\x06proto3'
  ,
  dependencies=[arg__services_dot_base_dot_v1_dot_base__pb2.DESCRIPTOR,])

_PREDICTION = _descriptor.EnumDescriptor(
  name='Prediction',
  full_name='arg_services.entailment.v1.Prediction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PREDICTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PREDICTION_ENTAILMENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PREDICTION_CONTRADICTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PREDICTION_NEUTRAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=438,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_PREDICTION)

Prediction = enum_type_wrapper.EnumTypeWrapper(_PREDICTION)
PREDICTION_UNSPECIFIED = 0
PREDICTION_ENTAILMENT = 1
PREDICTION_CONTRADICTION = 2
PREDICTION_NEUTRAL = 3



_ENTAILMENTREQUEST = _descriptor.Descriptor(
  name='EntailmentRequest',
  full_name='arg_services.entailment.v1.EntailmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='arg_services.entailment.v1.EntailmentRequest.language', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='premise', full_name='arg_services.entailment.v1.EntailmentRequest.premise', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claim', full_name='arg_services.entailment.v1.EntailmentRequest.claim', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=209,
)


_ENTAILMENTRESPONSE = _descriptor.Descriptor(
  name='EntailmentResponse',
  full_name='arg_services.entailment.v1.EntailmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='arg_services.entailment.v1.EntailmentResponse.prediction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='arg_services.entailment.v1.EntailmentResponse.details', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=345,
)


_DETAIL = _descriptor.Descriptor(
  name='Detail',
  full_name='arg_services.entailment.v1.Detail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='probability', full_name='arg_services.entailment.v1.Detail.probability', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='arg_services.entailment.v1.Detail.prediction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=436,
)

_ENTAILMENTREQUEST.fields_by_name['language'].enum_type = arg__services_dot_base_dot_v1_dot_base__pb2._LANGUAGE
_ENTAILMENTRESPONSE.fields_by_name['prediction'].enum_type = _PREDICTION
_ENTAILMENTRESPONSE.fields_by_name['details'].message_type = _DETAIL
_DETAIL.fields_by_name['prediction'].enum_type = _PREDICTION
DESCRIPTOR.message_types_by_name['EntailmentRequest'] = _ENTAILMENTREQUEST
DESCRIPTOR.message_types_by_name['EntailmentResponse'] = _ENTAILMENTRESPONSE
DESCRIPTOR.message_types_by_name['Detail'] = _DETAIL
DESCRIPTOR.enum_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntailmentRequest = _reflection.GeneratedProtocolMessageType('EntailmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENTAILMENTREQUEST,
  '__module__' : 'arg_services.entailment.v1.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.entailment.v1.EntailmentRequest)
  })
_sym_db.RegisterMessage(EntailmentRequest)

EntailmentResponse = _reflection.GeneratedProtocolMessageType('EntailmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENTAILMENTRESPONSE,
  '__module__' : 'arg_services.entailment.v1.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.entailment.v1.EntailmentResponse)
  })
_sym_db.RegisterMessage(EntailmentResponse)

Detail = _reflection.GeneratedProtocolMessageType('Detail', (_message.Message,), {
  'DESCRIPTOR' : _DETAIL,
  '__module__' : 'arg_services.entailment.v1.entailment_pb2'
  # @@protoc_insertion_point(class_scope:arg_services.entailment.v1.Detail)
  })
_sym_db.RegisterMessage(Detail)



_ENTAILMENTSERVICE = _descriptor.ServiceDescriptor(
  name='EntailmentService',
  full_name='arg_services.entailment.v1.EntailmentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=562,
  serialized_end=690,
  methods=[
  _descriptor.MethodDescriptor(
    name='Entailment',
    full_name='arg_services.entailment.v1.EntailmentService.Entailment',
    index=0,
    containing_service=None,
    input_type=_ENTAILMENTREQUEST,
    output_type=_ENTAILMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTAILMENTSERVICE)

DESCRIPTOR.services_by_name['EntailmentService'] = _ENTAILMENTSERVICE

# @@protoc_insertion_point(module_scope)
