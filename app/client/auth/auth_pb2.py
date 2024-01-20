# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\">\n\x12VerifyEmailRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12\x14\n\x0cverify_token\x18\x02 \x01(\t\"&\n\x13VerifyEmailResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"+\n\x15VerifyEmailNewRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\")\n\x16VerifyEmailNewResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\'\n\x0eRefreshRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"R\n\x0fRefreshResponse\x12\x12\n\ntoken_type\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\"%\n\rAccessRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"8\n\x0e\x41\x63\x63\x65ssResponse\x12\x0b\n\x03\x65xp\x18\x01 \x01(\x05\x12\x0b\n\x03sub\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"&\n\x13\x43reateTokensRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"W\n\x14\x43reateTokensResponse\x12\x12\n\ntoken_type\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t2\xd5\x02\n\x04\x41uth\x12\x44\n\x0bVerifyEmail\x12\x18.auth.VerifyEmailRequest\x1a\x19.auth.VerifyEmailResponse\"\x00\x12M\n\x0eVerifyEmailNew\x12\x1b.auth.VerifyEmailNewRequest\x1a\x1c.auth.VerifyEmailNewResponse\"\x00\x12\x38\n\x07Refresh\x12\x14.auth.RefreshRequest\x1a\x15.auth.RefreshResponse\"\x00\x12\x35\n\x06\x41\x63\x63\x65ss\x12\x13.auth.AccessRequest\x1a\x14.auth.AccessResponse\"\x00\x12G\n\x0c\x43reateTokens\x12\x19.auth.CreateTokensRequest\x1a\x1a.auth.CreateTokensResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VERIFYEMAILREQUEST']._serialized_start=20
  _globals['_VERIFYEMAILREQUEST']._serialized_end=82
  _globals['_VERIFYEMAILRESPONSE']._serialized_start=84
  _globals['_VERIFYEMAILRESPONSE']._serialized_end=122
  _globals['_VERIFYEMAILNEWREQUEST']._serialized_start=124
  _globals['_VERIFYEMAILNEWREQUEST']._serialized_end=167
  _globals['_VERIFYEMAILNEWRESPONSE']._serialized_start=169
  _globals['_VERIFYEMAILNEWRESPONSE']._serialized_end=210
  _globals['_REFRESHREQUEST']._serialized_start=212
  _globals['_REFRESHREQUEST']._serialized_end=251
  _globals['_REFRESHRESPONSE']._serialized_start=253
  _globals['_REFRESHRESPONSE']._serialized_end=335
  _globals['_ACCESSREQUEST']._serialized_start=337
  _globals['_ACCESSREQUEST']._serialized_end=374
  _globals['_ACCESSRESPONSE']._serialized_start=376
  _globals['_ACCESSRESPONSE']._serialized_end=432
  _globals['_CREATETOKENSREQUEST']._serialized_start=434
  _globals['_CREATETOKENSREQUEST']._serialized_end=472
  _globals['_CREATETOKENSRESPONSE']._serialized_start=474
  _globals['_CREATETOKENSRESPONSE']._serialized_end=561
  _globals['_AUTH']._serialized_start=564
  _globals['_AUTH']._serialized_end=905
# @@protoc_insertion_point(module_scope)
