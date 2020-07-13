# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log_files.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='log_files.proto',
  package='mavsdk.rpc.log_files',
  syntax='proto3',
  serialized_options=b'\n\023io.mavsdk.log_filesB\rLogFilesProto',
  serialized_pb=b'\n\x0flog_files.proto\x12\x14mavsdk.rpc.log_files\x1a\x14mavsdk_options.proto\"\x13\n\x11GetEntriesRequest\"\x82\x01\n\x12GetEntriesResponse\x12>\n\x10log_files_result\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.log_files.LogFilesResult\x12,\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x1b.mavsdk.rpc.log_files.Entry\";\n\x1fSubscribeDownloadLogFileRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04path\x18\x02 \x01(\t\"\x8f\x01\n\x17\x44ownloadLogFileResponse\x12>\n\x10log_files_result\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.log_files.LogFilesResult\x12\x34\n\x08progress\x18\x02 \x01(\x0b\x32\".mavsdk.rpc.log_files.ProgressData\")\n\x0cProgressData\x12\x19\n\x08progress\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"5\n\x05\x45ntry\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\r\"\x8b\x02\n\x0eLogFilesResult\x12;\n\x06result\x18\x01 \x01(\x0e\x32+.mavsdk.rpc.log_files.LogFilesResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xa7\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x0f\n\x0bRESULT_NEXT\x10\x02\x12\x16\n\x12RESULT_NO_LOGFILES\x10\x03\x12\x12\n\x0eRESULT_TIMEOUT\x10\x04\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x05\x12\x1b\n\x17RESULT_FILE_OPEN_FAILED\x10\x06\x32\x83\x02\n\x0fLogFilesService\x12\x61\n\nGetEntries\x12\'.mavsdk.rpc.log_files.GetEntriesRequest\x1a(.mavsdk.rpc.log_files.GetEntriesResponse\"\x00\x12\x8c\x01\n\x18SubscribeDownloadLogFile\x12\x35.mavsdk.rpc.log_files.SubscribeDownloadLogFileRequest\x1a-.mavsdk.rpc.log_files.DownloadLogFileResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x42$\n\x13io.mavsdk.log_filesB\rLogFilesProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_LOGFILESRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.log_files.LogFilesResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NEXT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_LOGFILES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_ARGUMENT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_FILE_OPEN_FAILED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=623,
  serialized_end=790,
)
_sym_db.RegisterEnumDescriptor(_LOGFILESRESULT_RESULT)


_GETENTRIESREQUEST = _descriptor.Descriptor(
  name='GetEntriesRequest',
  full_name='mavsdk.rpc.log_files.GetEntriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=63,
  serialized_end=82,
)


_GETENTRIESRESPONSE = _descriptor.Descriptor(
  name='GetEntriesResponse',
  full_name='mavsdk.rpc.log_files.GetEntriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_files_result', full_name='mavsdk.rpc.log_files.GetEntriesResponse.log_files_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='mavsdk.rpc.log_files.GetEntriesResponse.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=85,
  serialized_end=215,
)


_SUBSCRIBEDOWNLOADLOGFILEREQUEST = _descriptor.Descriptor(
  name='SubscribeDownloadLogFileRequest',
  full_name='mavsdk.rpc.log_files.SubscribeDownloadLogFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mavsdk.rpc.log_files.SubscribeDownloadLogFileRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='mavsdk.rpc.log_files.SubscribeDownloadLogFileRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=217,
  serialized_end=276,
)


_DOWNLOADLOGFILERESPONSE = _descriptor.Descriptor(
  name='DownloadLogFileResponse',
  full_name='mavsdk.rpc.log_files.DownloadLogFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_files_result', full_name='mavsdk.rpc.log_files.DownloadLogFileResponse.log_files_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='mavsdk.rpc.log_files.DownloadLogFileResponse.progress', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=279,
  serialized_end=422,
)


_PROGRESSDATA = _descriptor.Descriptor(
  name='ProgressData',
  full_name='mavsdk.rpc.log_files.ProgressData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='progress', full_name='mavsdk.rpc.log_files.ProgressData.progress', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\003NaN', file=DESCRIPTOR),
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
  serialized_start=424,
  serialized_end=465,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='mavsdk.rpc.log_files.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mavsdk.rpc.log_files.Entry.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='mavsdk.rpc.log_files.Entry.date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='mavsdk.rpc.log_files.Entry.size_bytes', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=467,
  serialized_end=520,
)


_LOGFILESRESULT = _descriptor.Descriptor(
  name='LogFilesResult',
  full_name='mavsdk.rpc.log_files.LogFilesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.log_files.LogFilesResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.log_files.LogFilesResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGFILESRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=790,
)

_GETENTRIESRESPONSE.fields_by_name['log_files_result'].message_type = _LOGFILESRESULT
_GETENTRIESRESPONSE.fields_by_name['entries'].message_type = _ENTRY
_DOWNLOADLOGFILERESPONSE.fields_by_name['log_files_result'].message_type = _LOGFILESRESULT
_DOWNLOADLOGFILERESPONSE.fields_by_name['progress'].message_type = _PROGRESSDATA
_LOGFILESRESULT.fields_by_name['result'].enum_type = _LOGFILESRESULT_RESULT
_LOGFILESRESULT_RESULT.containing_type = _LOGFILESRESULT
DESCRIPTOR.message_types_by_name['GetEntriesRequest'] = _GETENTRIESREQUEST
DESCRIPTOR.message_types_by_name['GetEntriesResponse'] = _GETENTRIESRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeDownloadLogFileRequest'] = _SUBSCRIBEDOWNLOADLOGFILEREQUEST
DESCRIPTOR.message_types_by_name['DownloadLogFileResponse'] = _DOWNLOADLOGFILERESPONSE
DESCRIPTOR.message_types_by_name['ProgressData'] = _PROGRESSDATA
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['LogFilesResult'] = _LOGFILESRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetEntriesRequest = _reflection.GeneratedProtocolMessageType('GetEntriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENTRIESREQUEST,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.GetEntriesRequest)
  })
_sym_db.RegisterMessage(GetEntriesRequest)

GetEntriesResponse = _reflection.GeneratedProtocolMessageType('GetEntriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETENTRIESRESPONSE,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.GetEntriesResponse)
  })
_sym_db.RegisterMessage(GetEntriesResponse)

SubscribeDownloadLogFileRequest = _reflection.GeneratedProtocolMessageType('SubscribeDownloadLogFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEDOWNLOADLOGFILEREQUEST,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.SubscribeDownloadLogFileRequest)
  })
_sym_db.RegisterMessage(SubscribeDownloadLogFileRequest)

DownloadLogFileResponse = _reflection.GeneratedProtocolMessageType('DownloadLogFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADLOGFILERESPONSE,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.DownloadLogFileResponse)
  })
_sym_db.RegisterMessage(DownloadLogFileResponse)

ProgressData = _reflection.GeneratedProtocolMessageType('ProgressData', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSDATA,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.ProgressData)
  })
_sym_db.RegisterMessage(ProgressData)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.Entry)
  })
_sym_db.RegisterMessage(Entry)

LogFilesResult = _reflection.GeneratedProtocolMessageType('LogFilesResult', (_message.Message,), {
  'DESCRIPTOR' : _LOGFILESRESULT,
  '__module__' : 'log_files_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.log_files.LogFilesResult)
  })
_sym_db.RegisterMessage(LogFilesResult)


DESCRIPTOR._options = None
_PROGRESSDATA.fields_by_name['progress']._options = None

_LOGFILESSERVICE = _descriptor.ServiceDescriptor(
  name='LogFilesService',
  full_name='mavsdk.rpc.log_files.LogFilesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=793,
  serialized_end=1052,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetEntries',
    full_name='mavsdk.rpc.log_files.LogFilesService.GetEntries',
    index=0,
    containing_service=None,
    input_type=_GETENTRIESREQUEST,
    output_type=_GETENTRIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeDownloadLogFile',
    full_name='mavsdk.rpc.log_files.LogFilesService.SubscribeDownloadLogFile',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIBEDOWNLOADLOGFILEREQUEST,
    output_type=_DOWNLOADLOGFILERESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGFILESSERVICE)

DESCRIPTOR.services_by_name['LogFilesService'] = _LOGFILESSERVICE

# @@protoc_insertion_point(module_scope)
