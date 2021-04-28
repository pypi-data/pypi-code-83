# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deepomatic/oef/protos/models/image/ocr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from deepomatic.oef.protos.models.image import backbones_pb2 as deepomatic_dot_oef_dot_protos_dot_models_dot_image_dot_backbones__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deepomatic/oef/protos/models/image/ocr.proto',
  package='deepomatic.oef.models.image.ocr',
  syntax='proto2',
  serialized_pb=_b('\n,deepomatic/oef/protos/models/image/ocr.proto\x12\x1f\x64\x65\x65pomatic.oef.models.image.ocr\x1a\x32\x64\x65\x65pomatic/oef/protos/models/image/backbones.proto\"\xec\x01\n\tAttention\x12 \n\x12use_autoregression\x18\x01 \x01(\x08:\x04true\x12\x1b\n\x0enum_lstm_units\x18\x02 \x01(\x05:\x03\x32\x35\x36\x12$\n\x16use_coordinate_feature\x18\x03 \x01(\x08:\x04true\x12\x1c\n\x11\x66\x65\x61ture_map_ratio\x18\x04 \x01(\x05:\x01\x38\x12\x1b\n\x0cweight_decay\x18\x05 \x01(\x02:\x05\x34\x65-05\x12!\n\x15lstm_state_clip_value\x18\x06 \x01(\x02:\x02\x31\x30\x12\x1c\n\x0flabel_smoothing\x18\x07 \x01(\x02:\x03\x30.1\"\xa3\x01\n\x03OCR\x12\x41\n\x08\x62\x61\x63kbone\x18\x01 \x02(\x0b\x32/.deepomatic.oef.models.image.backbones.Backbone\x12?\n\tattention\x18\x10 \x01(\x0b\x32*.deepomatic.oef.models.image.ocr.AttentionH\x00\x42\x18\n\x16meta_architecture_type')
  ,
  dependencies=[deepomatic_dot_oef_dot_protos_dot_models_dot_image_dot_backbones__pb2.DESCRIPTOR,])




_ATTENTION = _descriptor.Descriptor(
  name='Attention',
  full_name='deepomatic.oef.models.image.ocr.Attention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_autoregression', full_name='deepomatic.oef.models.image.ocr.Attention.use_autoregression', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_lstm_units', full_name='deepomatic.oef.models.image.ocr.Attention.num_lstm_units', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_coordinate_feature', full_name='deepomatic.oef.models.image.ocr.Attention.use_coordinate_feature', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_map_ratio', full_name='deepomatic.oef.models.image.ocr.Attention.feature_map_ratio', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_decay', full_name='deepomatic.oef.models.image.ocr.Attention.weight_decay', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(4e-05),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lstm_state_clip_value', full_name='deepomatic.oef.models.image.ocr.Attention.lstm_state_clip_value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(10),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_smoothing', full_name='deepomatic.oef.models.image.ocr.Attention.label_smoothing', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=370,
)


_OCR = _descriptor.Descriptor(
  name='OCR',
  full_name='deepomatic.oef.models.image.ocr.OCR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backbone', full_name='deepomatic.oef.models.image.ocr.OCR.backbone', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attention', full_name='deepomatic.oef.models.image.ocr.OCR.attention', index=1,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='meta_architecture_type', full_name='deepomatic.oef.models.image.ocr.OCR.meta_architecture_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=373,
  serialized_end=536,
)

_OCR.fields_by_name['backbone'].message_type = deepomatic_dot_oef_dot_protos_dot_models_dot_image_dot_backbones__pb2._BACKBONE
_OCR.fields_by_name['attention'].message_type = _ATTENTION
_OCR.oneofs_by_name['meta_architecture_type'].fields.append(
  _OCR.fields_by_name['attention'])
_OCR.fields_by_name['attention'].containing_oneof = _OCR.oneofs_by_name['meta_architecture_type']
DESCRIPTOR.message_types_by_name['Attention'] = _ATTENTION
DESCRIPTOR.message_types_by_name['OCR'] = _OCR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attention = _reflection.GeneratedProtocolMessageType('Attention', (_message.Message,), dict(
  DESCRIPTOR = _ATTENTION,
  __module__ = 'deepomatic.oef.protos.models.image.ocr_pb2'
  # @@protoc_insertion_point(class_scope:deepomatic.oef.models.image.ocr.Attention)
  ))
_sym_db.RegisterMessage(Attention)

OCR = _reflection.GeneratedProtocolMessageType('OCR', (_message.Message,), dict(
  DESCRIPTOR = _OCR,
  __module__ = 'deepomatic.oef.protos.models.image.ocr_pb2'
  # @@protoc_insertion_point(class_scope:deepomatic.oef.models.image.ocr.OCR)
  ))
_sym_db.RegisterMessage(OCR)


# @@protoc_insertion_point(module_scope)
