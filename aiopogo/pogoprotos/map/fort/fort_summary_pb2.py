# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/fort_summary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/fort_summary.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_pb=_b('\n&pogoprotos/map/fort/fort_summary.proto\x12\x13pogoprotos.map.fort\"o\n\x0b\x46ortSummary\x12\x17\n\x0f\x66ort_summary_id\x18\x01 \x01(\t\x12\"\n\x1alast_modified_timestamp_ms\x18\x02 \x01(\x03\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x62\x06proto3')
)




_FORTSUMMARY = _descriptor.Descriptor(
  name='FortSummary',
  full_name='pogoprotos.map.fort.FortSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_summary_id', full_name='pogoprotos.map.fort.FortSummary.fort_summary_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_timestamp_ms', full_name='pogoprotos.map.fort.FortSummary.last_modified_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.map.fort.FortSummary.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.map.fort.FortSummary.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['FortSummary'] = _FORTSUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortSummary = _reflection.GeneratedProtocolMessageType('FortSummary', (_message.Message,), dict(
  DESCRIPTOR = _FORTSUMMARY,
  __module__ = 'pogoprotos.map.fort.fort_summary_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.FortSummary)
  ))
_sym_db.RegisterMessage(FortSummary)


# @@protoc_insertion_point(module_scope)
