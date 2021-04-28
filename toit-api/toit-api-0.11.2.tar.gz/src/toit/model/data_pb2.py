# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: toit/model/data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='toit/model/data.proto',
  package='toit.model',
  syntax='proto3',
  serialized_options=b'\n\030io.toit.proto.toit.modelB\tDataProtoZ&github.com/toitware/api.git/toit/model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15toit/model/data.proto\x12\ntoit.model\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9c\x02\n\x0bMetricsData\x12\r\n\x05names\x18\x01 \x03(\x0c\x12+\n\x06gauges\x18\x02 \x03(\x0b\x32\x1b.toit.model.GuageMetricData\x12/\n\x08\x63ounters\x18\x03 \x03(\x0b\x32\x1d.toit.model.CounterMetricData\x12-\n\x05plots\x18\x04 \x03(\x0b\x32\x1a.toit.model.PlotMetricDataB\x02\x18\x01\x12\x33\n\nhistograms\x18\x05 \x03(\x0b\x32\x1f.toit.model.HistogramMetricData\"<\n\x05Level\x12\x0f\n\x0b\x44\x45\x42UG_LEVEL\x10\x00\x12\x0e\n\nINFO_LEVEL\x10\x05\x12\x12\n\x0e\x43RITICAL_LEVEL\x10\n\"\xf5\x01\n\x0fGuageMetricData\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x12\n\nname_index\x18\x02 \x01(\r\x12/\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01\x12\x33\n\x04tags\x18\x04 \x03(\x0b\x32%.toit.model.GuageMetricData.TagsEntry\x12,\n\x05level\x18\x05 \x01(\x0e\x32\x1d.toit.model.MetricsData.Level\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xed\x01\n\x11\x43ounterMetricData\x12\x12\n\nname_index\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x10\n\x04mean\x18\x03 \x01(\x01\x42\x02\x18\x01\x12\x11\n\x05stdev\x18\x04 \x01(\x01\x42\x02\x18\x01\x12\x35\n\x04tags\x18\x05 \x03(\x0b\x32\'.toit.model.CounterMetricData.TagsEntry\x12,\n\x05level\x18\x06 \x01(\x0e\x32\x1d.toit.model.MetricsData.Level\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xc5\x01\n\x0ePlotMetricData\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x12\n\nname_index\x18\x02 \x01(\r\x12+\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x04tags\x18\x04 \x03(\x0b\x32$.toit.model.PlotMetricData.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01:\x02\x18\x01\"\xa9\x02\n\x13HistogramMetricData\x12\x12\n\nname_index\x18\x01 \x01(\r\x12;\n\x06values\x18\x02 \x03(\x0b\x32+.toit.model.HistogramMetricData.ValuesEntry\x12\x37\n\x04tags\x18\x03 \x03(\x0b\x32).toit.model.HistogramMetricData.TagsEntry\x12,\n\x05level\x18\x04 \x01(\x0e\x32\x1d.toit.model.MetricsData.Level\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"(\n\tTopicData\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xd6\x03\n\x07LogData\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.toit.model.LogData.Type\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t\x12(\n\x05level\x18\x04 \x01(\x0e\x32\x19.toit.model.LogData.Level\x12\r\n\x05names\x18\x05 \x03(\t\x12+\n\x04tags\x18\x06 \x03(\x0b\x32\x1d.toit.model.LogData.TagsEntry\x1a\x43\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"l\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05PRINT\x10\x01\x12\x11\n\rPROCESS_START\x10\x02\x12\x10\n\x0cPROCESS_STOP\x10\x03\x12\x0f\n\x0bSTACK_TRACE\x10\x04\x12\x08\n\x04\x42OOT\x10\x05\x12\x0c\n\x08SHUTDOWN\x10\x06\"k\n\x05Level\x12\x0f\n\x0bPRINT_LEVEL\x10\x00\x12\x0f\n\x0b\x44\x45\x42UG_LEVEL\x10\x01\x12\x0e\n\nINFO_LEVEL\x10\x02\x12\x0e\n\nWARN_LEVEL\x10\x03\x12\x0f\n\x0b\x45RROR_LEVEL\x10\x04\x12\x0f\n\x0b\x46\x41TAL_LEVEL\x10\x05\x42M\n\x18io.toit.proto.toit.modelB\tDataProtoZ&github.com/toitware/api.git/toit/modelb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_METRICSDATA_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='toit.model.MetricsData.Level',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG_LEVEL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO_LEVEL', index=1, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL_LEVEL', index=2, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=325,
  serialized_end=385,
)
_sym_db.RegisterEnumDescriptor(_METRICSDATA_LEVEL)

_LOGDATA_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='toit.model.LogData.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRINT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESS_START', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESS_STOP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STACK_TRACE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1671,
  serialized_end=1779,
)
_sym_db.RegisterEnumDescriptor(_LOGDATA_TYPE)

_LOGDATA_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='toit.model.LogData.Level',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRINT_LEVEL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEBUG_LEVEL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO_LEVEL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARN_LEVEL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEVEL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FATAL_LEVEL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1781,
  serialized_end=1888,
)
_sym_db.RegisterEnumDescriptor(_LOGDATA_LEVEL)


_METRICSDATA = _descriptor.Descriptor(
  name='MetricsData',
  full_name='toit.model.MetricsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='toit.model.MetricsData.names', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gauges', full_name='toit.model.MetricsData.gauges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counters', full_name='toit.model.MetricsData.counters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plots', full_name='toit.model.MetricsData.plots', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='histograms', full_name='toit.model.MetricsData.histograms', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICSDATA_LEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=385,
)


_GUAGEMETRICDATA_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='toit.model.GuageMetricData.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.GuageMetricData.TagsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.GuageMetricData.TagsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=633,
)

_GUAGEMETRICDATA = _descriptor.Descriptor(
  name='GuageMetricData',
  full_name='toit.model.GuageMetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.GuageMetricData.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name_index', full_name='toit.model.GuageMetricData.name_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='toit.model.GuageMetricData.created', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='toit.model.GuageMetricData.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='toit.model.GuageMetricData.level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GUAGEMETRICDATA_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=633,
)


_COUNTERMETRICDATA_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='toit.model.CounterMetricData.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.CounterMetricData.TagsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.CounterMetricData.TagsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=633,
)

_COUNTERMETRICDATA = _descriptor.Descriptor(
  name='CounterMetricData',
  full_name='toit.model.CounterMetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name_index', full_name='toit.model.CounterMetricData.name_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='toit.model.CounterMetricData.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mean', full_name='toit.model.CounterMetricData.mean', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stdev', full_name='toit.model.CounterMetricData.stdev', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='toit.model.CounterMetricData.tags', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='toit.model.CounterMetricData.level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COUNTERMETRICDATA_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=873,
)


_PLOTMETRICDATA_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='toit.model.PlotMetricData.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.PlotMetricData.TagsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.PlotMetricData.TagsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=633,
)

_PLOTMETRICDATA = _descriptor.Descriptor(
  name='PlotMetricData',
  full_name='toit.model.PlotMetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.PlotMetricData.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name_index', full_name='toit.model.PlotMetricData.name_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='toit.model.PlotMetricData.created', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='toit.model.PlotMetricData.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PLOTMETRICDATA_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=1073,
)


_HISTOGRAMMETRICDATA_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='toit.model.HistogramMetricData.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.HistogramMetricData.ValuesEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.HistogramMetricData.ValuesEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1283,
  serialized_end=1328,
)

_HISTOGRAMMETRICDATA_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='toit.model.HistogramMetricData.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.HistogramMetricData.TagsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.HistogramMetricData.TagsEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=633,
)

_HISTOGRAMMETRICDATA = _descriptor.Descriptor(
  name='HistogramMetricData',
  full_name='toit.model.HistogramMetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name_index', full_name='toit.model.HistogramMetricData.name_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='toit.model.HistogramMetricData.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='toit.model.HistogramMetricData.tags', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='toit.model.HistogramMetricData.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HISTOGRAMMETRICDATA_VALUESENTRY, _HISTOGRAMMETRICDATA_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1373,
)


_TOPICDATA = _descriptor.Descriptor(
  name='TopicData',
  full_name='toit.model.TopicData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='toit.model.TopicData.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='toit.model.TopicData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1375,
  serialized_end=1415,
)


_LOGDATA_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='toit.model.LogData.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='toit.model.LogData.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='toit.model.LogData.TagsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1602,
  serialized_end=1669,
)

_LOGDATA = _descriptor.Descriptor(
  name='LogData',
  full_name='toit.model.LogData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='toit.model.LogData.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='toit.model.LogData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='toit.model.LogData.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='toit.model.LogData.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='names', full_name='toit.model.LogData.names', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='toit.model.LogData.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOGDATA_TAGSENTRY, ],
  enum_types=[
    _LOGDATA_TYPE,
    _LOGDATA_LEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1418,
  serialized_end=1888,
)

_METRICSDATA.fields_by_name['gauges'].message_type = _GUAGEMETRICDATA
_METRICSDATA.fields_by_name['counters'].message_type = _COUNTERMETRICDATA
_METRICSDATA.fields_by_name['plots'].message_type = _PLOTMETRICDATA
_METRICSDATA.fields_by_name['histograms'].message_type = _HISTOGRAMMETRICDATA
_METRICSDATA_LEVEL.containing_type = _METRICSDATA
_GUAGEMETRICDATA_TAGSENTRY.containing_type = _GUAGEMETRICDATA
_GUAGEMETRICDATA.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GUAGEMETRICDATA.fields_by_name['tags'].message_type = _GUAGEMETRICDATA_TAGSENTRY
_GUAGEMETRICDATA.fields_by_name['level'].enum_type = _METRICSDATA_LEVEL
_COUNTERMETRICDATA_TAGSENTRY.containing_type = _COUNTERMETRICDATA
_COUNTERMETRICDATA.fields_by_name['tags'].message_type = _COUNTERMETRICDATA_TAGSENTRY
_COUNTERMETRICDATA.fields_by_name['level'].enum_type = _METRICSDATA_LEVEL
_PLOTMETRICDATA_TAGSENTRY.containing_type = _PLOTMETRICDATA
_PLOTMETRICDATA.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PLOTMETRICDATA.fields_by_name['tags'].message_type = _PLOTMETRICDATA_TAGSENTRY
_HISTOGRAMMETRICDATA_VALUESENTRY.containing_type = _HISTOGRAMMETRICDATA
_HISTOGRAMMETRICDATA_TAGSENTRY.containing_type = _HISTOGRAMMETRICDATA
_HISTOGRAMMETRICDATA.fields_by_name['values'].message_type = _HISTOGRAMMETRICDATA_VALUESENTRY
_HISTOGRAMMETRICDATA.fields_by_name['tags'].message_type = _HISTOGRAMMETRICDATA_TAGSENTRY
_HISTOGRAMMETRICDATA.fields_by_name['level'].enum_type = _METRICSDATA_LEVEL
_LOGDATA_TAGSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LOGDATA_TAGSENTRY.containing_type = _LOGDATA
_LOGDATA.fields_by_name['type'].enum_type = _LOGDATA_TYPE
_LOGDATA.fields_by_name['level'].enum_type = _LOGDATA_LEVEL
_LOGDATA.fields_by_name['tags'].message_type = _LOGDATA_TAGSENTRY
_LOGDATA_TYPE.containing_type = _LOGDATA
_LOGDATA_LEVEL.containing_type = _LOGDATA
DESCRIPTOR.message_types_by_name['MetricsData'] = _METRICSDATA
DESCRIPTOR.message_types_by_name['GuageMetricData'] = _GUAGEMETRICDATA
DESCRIPTOR.message_types_by_name['CounterMetricData'] = _COUNTERMETRICDATA
DESCRIPTOR.message_types_by_name['PlotMetricData'] = _PLOTMETRICDATA
DESCRIPTOR.message_types_by_name['HistogramMetricData'] = _HISTOGRAMMETRICDATA
DESCRIPTOR.message_types_by_name['TopicData'] = _TOPICDATA
DESCRIPTOR.message_types_by_name['LogData'] = _LOGDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricsData = _reflection.GeneratedProtocolMessageType('MetricsData', (_message.Message,), {
  'DESCRIPTOR' : _METRICSDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.MetricsData)
  })
_sym_db.RegisterMessage(MetricsData)

GuageMetricData = _reflection.GeneratedProtocolMessageType('GuageMetricData', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GUAGEMETRICDATA_TAGSENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.GuageMetricData.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _GUAGEMETRICDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.GuageMetricData)
  })
_sym_db.RegisterMessage(GuageMetricData)
_sym_db.RegisterMessage(GuageMetricData.TagsEntry)

CounterMetricData = _reflection.GeneratedProtocolMessageType('CounterMetricData', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTERMETRICDATA_TAGSENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.CounterMetricData.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTERMETRICDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.CounterMetricData)
  })
_sym_db.RegisterMessage(CounterMetricData)
_sym_db.RegisterMessage(CounterMetricData.TagsEntry)

PlotMetricData = _reflection.GeneratedProtocolMessageType('PlotMetricData', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLOTMETRICDATA_TAGSENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.PlotMetricData.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _PLOTMETRICDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.PlotMetricData)
  })
_sym_db.RegisterMessage(PlotMetricData)
_sym_db.RegisterMessage(PlotMetricData.TagsEntry)

HistogramMetricData = _reflection.GeneratedProtocolMessageType('HistogramMetricData', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HISTOGRAMMETRICDATA_VALUESENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.HistogramMetricData.ValuesEntry)
    })
  ,

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HISTOGRAMMETRICDATA_TAGSENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.HistogramMetricData.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _HISTOGRAMMETRICDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.HistogramMetricData)
  })
_sym_db.RegisterMessage(HistogramMetricData)
_sym_db.RegisterMessage(HistogramMetricData.ValuesEntry)
_sym_db.RegisterMessage(HistogramMetricData.TagsEntry)

TopicData = _reflection.GeneratedProtocolMessageType('TopicData', (_message.Message,), {
  'DESCRIPTOR' : _TOPICDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.TopicData)
  })
_sym_db.RegisterMessage(TopicData)

LogData = _reflection.GeneratedProtocolMessageType('LogData', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGDATA_TAGSENTRY,
    '__module__' : 'toit.model.data_pb2'
    # @@protoc_insertion_point(class_scope:toit.model.LogData.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _LOGDATA,
  '__module__' : 'toit.model.data_pb2'
  # @@protoc_insertion_point(class_scope:toit.model.LogData)
  })
_sym_db.RegisterMessage(LogData)
_sym_db.RegisterMessage(LogData.TagsEntry)


DESCRIPTOR._options = None
_METRICSDATA.fields_by_name['plots']._options = None
_GUAGEMETRICDATA_TAGSENTRY._options = None
_GUAGEMETRICDATA.fields_by_name['created']._options = None
_COUNTERMETRICDATA_TAGSENTRY._options = None
_COUNTERMETRICDATA.fields_by_name['mean']._options = None
_COUNTERMETRICDATA.fields_by_name['stdev']._options = None
_PLOTMETRICDATA_TAGSENTRY._options = None
_PLOTMETRICDATA._options = None
_HISTOGRAMMETRICDATA_VALUESENTRY._options = None
_HISTOGRAMMETRICDATA_TAGSENTRY._options = None
_LOGDATA_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)
