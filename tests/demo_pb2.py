# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto

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
  name='demo.proto',
  package='demo',
  syntax='proto3',
  serialized_pb=_b('\n\ndemo.proto\x12\x04\x64\x65mo\"O\n\x06Record\x12\x0b\n\x03int\x18\x01 \x01(\x03\x12\r\n\x05\x66loat\x18\x02 \x01(\x02\x12\x0b\n\x03rep\x18\x1b \x03(\x03\x12\x1c\n\x06nested\x18\x1c \x01(\x0b\x32\x0c.demo.Nested\"+\n\nCollection\x12\x1d\n\x07records\x18\x01 \x03(\x0b\x32\x0c.demo.Record\"$\n\x06Nested\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x02\x12\x0c\n\x04more\x18\x02 \x01(\x02\x42\x02H\x03\x62\x06proto3')
)




_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='demo.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int', full_name='demo.Record.int', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float', full_name='demo.Record.float', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rep', full_name='demo.Record.rep', index=2,
      number=27, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nested', full_name='demo.Record.nested', index=3,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=99,
)


_COLLECTION = _descriptor.Descriptor(
  name='Collection',
  full_name='demo.Collection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='demo.Collection.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=101,
  serialized_end=144,
)


_NESTED = _descriptor.Descriptor(
  name='Nested',
  full_name='demo.Nested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='demo.Nested.data', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='more', full_name='demo.Nested.more', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=146,
  serialized_end=182,
)

_RECORD.fields_by_name['nested'].message_type = _NESTED
_COLLECTION.fields_by_name['records'].message_type = _RECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['Collection'] = _COLLECTION
DESCRIPTOR.message_types_by_name['Nested'] = _NESTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Record)
  ))
_sym_db.RegisterMessage(Record)

Collection = _reflection.GeneratedProtocolMessageType('Collection', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTION,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Collection)
  ))
_sym_db.RegisterMessage(Collection)

Nested = _reflection.GeneratedProtocolMessageType('Nested', (_message.Message,), dict(
  DESCRIPTOR = _NESTED,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:demo.Nested)
  ))
_sym_db.RegisterMessage(Nested)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
