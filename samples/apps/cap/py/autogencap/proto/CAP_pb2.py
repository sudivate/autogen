# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CAP.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tCAP.proto"C\n\x05\x45rror\x12\x18\n\x04\x63ode\x18\x01 \x01(\x0e\x32\n.ErrorCode\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message"i\n\tActorInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\tnamespace\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x0c\n\n_namespaceB\x0e\n\x0c_description"3\n\x11\x41\x63torRegistration\x12\x1e\n\nactor_info\x18\x01 \x01(\x0b\x32\n.ActorInfo"A\n\x0b\x41\x63torLookup\x12#\n\nactor_info\x18\x01 \x01(\x0b\x32\n.ActorInfoH\x00\x88\x01\x01\x42\r\n\x0b_actor_info"4\n\x13\x41\x63torInfoCollection\x12\x1d\n\tinfo_coll\x18\x01 \x03(\x0b\x32\n.ActorInfo"X\n\x13\x41\x63torLookupResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12(\n\x05\x61\x63tor\x18\x02 \x01(\x0b\x32\x14.ActorInfoCollectionH\x00\x88\x01\x01\x42\x08\n\x06_actor"\x06\n\x04Ping"\x06\n\x04Pong*O\n\tErrorCode\x12\t\n\x05\x45\x43_OK\x10\x00\x12\x10\n\x0c\x45\x43_NOT_FOUND\x10\x01\x12\x15\n\x11\x45\x43_ALREADY_EXISTS\x10\x02\x12\n\n\x06\x45\x43_MAX\x10\x02\x1a\x02\x10\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "CAP_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_ERRORCODE"]._options = None
    _globals["_ERRORCODE"]._serialized_options = b"\020\001"
    _globals["_ERRORCODE"]._serialized_start = 469
    _globals["_ERRORCODE"]._serialized_end = 548
    _globals["_ERROR"]._serialized_start = 13
    _globals["_ERROR"]._serialized_end = 80
    _globals["_ACTORINFO"]._serialized_start = 82
    _globals["_ACTORINFO"]._serialized_end = 187
    _globals["_ACTORREGISTRATION"]._serialized_start = 189
    _globals["_ACTORREGISTRATION"]._serialized_end = 240
    _globals["_ACTORLOOKUP"]._serialized_start = 242
    _globals["_ACTORLOOKUP"]._serialized_end = 307
    _globals["_ACTORINFOCOLLECTION"]._serialized_start = 309
    _globals["_ACTORINFOCOLLECTION"]._serialized_end = 361
    _globals["_ACTORLOOKUPRESPONSE"]._serialized_start = 363
    _globals["_ACTORLOOKUPRESPONSE"]._serialized_end = 451
    _globals["_PING"]._serialized_start = 453
    _globals["_PING"]._serialized_end = 459
    _globals["_PONG"]._serialized_start = 461
    _globals["_PONG"]._serialized_end = 467
# @@protoc_insertion_point(module_scope)
