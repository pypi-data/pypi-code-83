# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trdb2chatbot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trdb2chatbot.proto',
  package='tradingpb',
  syntax='proto3',
  serialized_options=b'Z&github.com/zhs007/tradingdb2/tradingpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12trdb2chatbot.proto\x12\ttradingpb\"\r\n\x0b\x43hatBotData\"\x19\n\x08UserData\x12\r\n\x05token\x18\x01 \x01(\tB(Z&github.com/zhs007/tradingdb2/tradingpbb\x06proto3'
)




_CHATBOTDATA = _descriptor.Descriptor(
  name='ChatBotData',
  full_name='tradingpb.ChatBotData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=33,
  serialized_end=46,
)


_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='tradingpb.UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='tradingpb.UserData.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['ChatBotData'] = _CHATBOTDATA
DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChatBotData = _reflection.GeneratedProtocolMessageType('ChatBotData', (_message.Message,), {
  'DESCRIPTOR' : _CHATBOTDATA,
  '__module__' : 'trdb2chatbot_pb2'
  # @@protoc_insertion_point(class_scope:tradingpb.ChatBotData)
  })
_sym_db.RegisterMessage(ChatBotData)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'trdb2chatbot_pb2'
  # @@protoc_insertion_point(class_scope:tradingpb.UserData)
  })
_sym_db.RegisterMessage(UserData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
