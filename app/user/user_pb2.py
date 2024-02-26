# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"*\n\x17UserBoxerProfileRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xcf\x01\n\x18UserBoxerProfileResponse\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x10\n\x08\x62irthday\x18\x04 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x0e\n\x06weight\x18\x07 \x01(\x01\x12\x0e\n\x06height\x18\x08 \x01(\x01\x12\x1c\n\x14\x61thletic_distinction\x18\t \x01(\t\x12\x0e\n\x06\x61vatar\x18\n \x01(\t\"\xee\x04\n\rBoxersRequest\x12\x17\n\nfirst_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tlast_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04\x63lub\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06region\x18\x05 \x01(\tH\x04\x88\x01\x01\x12!\n\x14\x61thletic_distinction\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x10\n\x03sex\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x17\n\nmin_weight\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12\x17\n\nmax_weight\x18\t \x01(\x01H\x08\x88\x01\x01\x12\x17\n\nmin_height\x18\n \x01(\x01H\t\x88\x01\x01\x12\x17\n\nmax_height\x18\x0b \x01(\x01H\n\x88\x01\x01\x12\x14\n\x07min_age\x18\x0c \x01(\x05H\x0b\x88\x01\x01\x12\x14\n\x07max_age\x18\r \x01(\x05H\x0c\x88\x01\x01\x12\x19\n\x0cmin_birthday\x18\x0e \x01(\tH\r\x88\x01\x01\x12\x19\n\x0cmax_birthday\x18\x0f \x01(\tH\x0e\x88\x01\x01\x12\x0c\n\x04page\x18\x10 \x01(\x05\x12\x11\n\tpage_size\x18\x11 \x01(\x05\x42\r\n\x0b_first_nameB\x0c\n\n_last_nameB\x07\n\x05_clubB\n\n\x08_countryB\t\n\x07_regionB\x17\n\x15_athletic_distinctionB\x06\n\x04_sexB\r\n\x0b_min_weightB\r\n\x0b_max_weightB\r\n\x0b_min_heightB\r\n\x0b_max_heightB\n\n\x08_min_ageB\n\n\x08_max_ageB\x0f\n\r_min_birthdayB\x0f\n\r_max_birthday\"\xb6\x01\n\x0e\x42oxersResponse\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0c\n\x04\x63lub\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0e\n\x06weight\x18\x06 \x01(\x01\x12\x10\n\x08\x62irthday\x18\x07 \x01(\t\x12\x1c\n\x14\x61thletic_distinction\x18\x08 \x01(\t\x12\x0e\n\x06\x61vatar\x18\t \x01(\t\"c\n\x11UploadFileRequest\x12\x14\n\x0c\x66ile_content\x18\x01 \x01(\x0c\x12\x11\n\tis_avatar\x18\x02 \x01(\x08\x12\x14\n\x0c\x63ontent_type\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"&\n\x13UpdateBoxerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9b\x01\n\rSignupRequest\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x01 \x01(\t\x12\x19\n\x0cphone_number\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65mail\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x18\n\x10password_confirm\x18\x05 \x01(\tB\x0f\n\r_phone_numberB\x08\n\x06_email\"!\n\x0eSignupResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"k\n\rSigninRequest\x12\x12\n\x05\x65mail\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cphone_number\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x08password\x18\x03 \x01(\tB\x08\n\x06_emailB\x0f\n\r_phone_number\"Q\n\x0eSigninResponse\x12\x12\n\ntoken_type\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\"v\n\x15\x43hangePasswordRequest\x12\x18\n\x10\x63urrent_password\x18\x01 \x01(\t\x12\x14\n\x0cnew_password\x18\x02 \x01(\t\x12\x1c\n\x14new_password_confirm\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"Y\n\x16\x43hangePasswordResponse\x12\x12\n\ntoken_type\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\"\xbf\x02\n\x18UpdateUserProfileRequest\x12\x17\n\nfirst_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tlast_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03sex\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bmiddle_name\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08\x62irthday\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x63ountry\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x13\n\x06region\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x11\n\x04\x63ity\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x0f\n\x07user_id\x18\t \x01(\tB\r\n\x0b_first_nameB\x0c\n\n_last_nameB\x06\n\x04_sexB\x0e\n\x0c_middle_nameB\x0b\n\t_birthdayB\n\n\x08_countryB\t\n\x07_regionB\x07\n\x05_city\",\n\x19UpdateUserProfileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"%\n\x12UploadFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xa1\x01\n\x12UpdateBoxerRequest\x12\x13\n\x06weight\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x13\n\x06height\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12!\n\x14\x61thletic_distinction\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x0f\n\x07user_id\x18\x04 \x01(\tB\t\n\x07_weightB\t\n\x07_heightB\x17\n\x15_athletic_distinction\"7\n\x0e\x41\x64\x64RoleRequest\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"\"\n\x0f\x41\x64\x64RoleResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"$\n\x11\x44\x65leteUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xaf\x05\n\x04User\x12\x35\n\x06Signup\x12\x13.user.SignupRequest\x1a\x14.user.SignupResponse\"\x00\x12\x35\n\x06Signin\x12\x13.user.SigninRequest\x1a\x14.user.SigninResponse\"\x00\x12M\n\x0e\x43hangePassword\x12\x1b.user.ChangePasswordRequest\x1a\x1c.user.ChangePasswordResponse\"\x00\x12V\n\x11UpdateUserProfile\x12\x1e.user.UpdateUserProfileRequest\x1a\x1f.user.UpdateUserProfileResponse\"\x00\x12\x44\n\x0bUpdateBoxer\x12\x18.user.UpdateBoxerRequest\x1a\x19.user.UpdateBoxerResponse\"\x00\x12\x38\n\x07\x41\x64\x64Role\x12\x14.user.AddRoleRequest\x1a\x15.user.AddRoleResponse\"\x00\x12\x41\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\"\x00\x12\x41\n\nUploadFile\x12\x17.user.UploadFileRequest\x1a\x18.user.UploadFileResponse\"\x00\x12S\n\x10UserBoxerProfile\x12\x1d.user.UserBoxerProfileRequest\x1a\x1e.user.UserBoxerProfileResponse\"\x00\x12\x37\n\x06\x42oxers\x12\x13.user.BoxersRequest\x1a\x14.user.BoxersResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERBOXERPROFILEREQUEST']._serialized_start=20
  _globals['_USERBOXERPROFILEREQUEST']._serialized_end=62
  _globals['_USERBOXERPROFILERESPONSE']._serialized_start=65
  _globals['_USERBOXERPROFILERESPONSE']._serialized_end=272
  _globals['_BOXERSREQUEST']._serialized_start=275
  _globals['_BOXERSREQUEST']._serialized_end=897
  _globals['_BOXERSRESPONSE']._serialized_start=900
  _globals['_BOXERSRESPONSE']._serialized_end=1082
  _globals['_UPLOADFILEREQUEST']._serialized_start=1084
  _globals['_UPLOADFILEREQUEST']._serialized_end=1183
  _globals['_UPDATEBOXERRESPONSE']._serialized_start=1185
  _globals['_UPDATEBOXERRESPONSE']._serialized_end=1223
  _globals['_SIGNUPREQUEST']._serialized_start=1226
  _globals['_SIGNUPREQUEST']._serialized_end=1381
  _globals['_SIGNUPRESPONSE']._serialized_start=1383
  _globals['_SIGNUPRESPONSE']._serialized_end=1416
  _globals['_SIGNINREQUEST']._serialized_start=1418
  _globals['_SIGNINREQUEST']._serialized_end=1525
  _globals['_SIGNINRESPONSE']._serialized_start=1527
  _globals['_SIGNINRESPONSE']._serialized_end=1608
  _globals['_CHANGEPASSWORDREQUEST']._serialized_start=1610
  _globals['_CHANGEPASSWORDREQUEST']._serialized_end=1728
  _globals['_CHANGEPASSWORDRESPONSE']._serialized_start=1730
  _globals['_CHANGEPASSWORDRESPONSE']._serialized_end=1819
  _globals['_UPDATEUSERPROFILEREQUEST']._serialized_start=1822
  _globals['_UPDATEUSERPROFILEREQUEST']._serialized_end=2141
  _globals['_UPDATEUSERPROFILERESPONSE']._serialized_start=2143
  _globals['_UPDATEUSERPROFILERESPONSE']._serialized_end=2187
  _globals['_UPLOADFILERESPONSE']._serialized_start=2189
  _globals['_UPLOADFILERESPONSE']._serialized_end=2226
  _globals['_UPDATEBOXERREQUEST']._serialized_start=2229
  _globals['_UPDATEBOXERREQUEST']._serialized_end=2390
  _globals['_ADDROLEREQUEST']._serialized_start=2392
  _globals['_ADDROLEREQUEST']._serialized_end=2447
  _globals['_ADDROLERESPONSE']._serialized_start=2449
  _globals['_ADDROLERESPONSE']._serialized_end=2483
  _globals['_DELETEUSERREQUEST']._serialized_start=2485
  _globals['_DELETEUSERREQUEST']._serialized_end=2521
  _globals['_DELETEUSERRESPONSE']._serialized_start=2523
  _globals['_DELETEUSERRESPONSE']._serialized_end=2560
  _globals['_USER']._serialized_start=2563
  _globals['_USER']._serialized_end=3250
# @@protoc_insertion_point(module_scope)
