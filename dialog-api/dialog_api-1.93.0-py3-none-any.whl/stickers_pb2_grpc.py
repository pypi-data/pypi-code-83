# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import miscellaneous_pb2 as miscellaneous__pb2
from . import stickers_pb2 as stickers__pb2


class StickersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadOwnStickers = channel.unary_unary(
                '/dialog.Stickers/LoadOwnStickers',
                request_serializer=stickers__pb2.RequestLoadOwnStickers.SerializeToString,
                response_deserializer=stickers__pb2.ResponseLoadOwnStickers.FromString,
                )
        self.LoadAcesssibleStickers = channel.unary_unary(
                '/dialog.Stickers/LoadAcesssibleStickers',
                request_serializer=stickers__pb2.RequestLoadAcesssibleStickers.SerializeToString,
                response_deserializer=stickers__pb2.ResponseLoadAcesssibleStickers.FromString,
                )
        self.AddStickerPackReference = channel.unary_unary(
                '/dialog.Stickers/AddStickerPackReference',
                request_serializer=stickers__pb2.RequestAddStickerPackReference.SerializeToString,
                response_deserializer=miscellaneous__pb2.ResponseSeq.FromString,
                )
        self.RemoveStickerPackReference = channel.unary_unary(
                '/dialog.Stickers/RemoveStickerPackReference',
                request_serializer=stickers__pb2.RequestRemoveStickerPackReference.SerializeToString,
                response_deserializer=miscellaneous__pb2.ResponseSeq.FromString,
                )
        self.AddStickerCollection = channel.unary_unary(
                '/dialog.Stickers/AddStickerCollection',
                request_serializer=stickers__pb2.RequestAddStickerCollection.SerializeToString,
                response_deserializer=miscellaneous__pb2.ResponseSeq.FromString,
                )
        self.RemoveStickerCollection = channel.unary_unary(
                '/dialog.Stickers/RemoveStickerCollection',
                request_serializer=stickers__pb2.RequestRemoveStickerCollection.SerializeToString,
                response_deserializer=miscellaneous__pb2.ResponseSeq.FromString,
                )
        self.LoadStickerCollection = channel.unary_unary(
                '/dialog.Stickers/LoadStickerCollection',
                request_serializer=stickers__pb2.RequestLoadStickerCollection.SerializeToString,
                response_deserializer=stickers__pb2.ResponseLoadStickerCollection.FromString,
                )


class StickersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LoadOwnStickers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadAcesssibleStickers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddStickerPackReference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveStickerPackReference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddStickerCollection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveStickerCollection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadStickerCollection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StickersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadOwnStickers': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadOwnStickers,
                    request_deserializer=stickers__pb2.RequestLoadOwnStickers.FromString,
                    response_serializer=stickers__pb2.ResponseLoadOwnStickers.SerializeToString,
            ),
            'LoadAcesssibleStickers': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadAcesssibleStickers,
                    request_deserializer=stickers__pb2.RequestLoadAcesssibleStickers.FromString,
                    response_serializer=stickers__pb2.ResponseLoadAcesssibleStickers.SerializeToString,
            ),
            'AddStickerPackReference': grpc.unary_unary_rpc_method_handler(
                    servicer.AddStickerPackReference,
                    request_deserializer=stickers__pb2.RequestAddStickerPackReference.FromString,
                    response_serializer=miscellaneous__pb2.ResponseSeq.SerializeToString,
            ),
            'RemoveStickerPackReference': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveStickerPackReference,
                    request_deserializer=stickers__pb2.RequestRemoveStickerPackReference.FromString,
                    response_serializer=miscellaneous__pb2.ResponseSeq.SerializeToString,
            ),
            'AddStickerCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.AddStickerCollection,
                    request_deserializer=stickers__pb2.RequestAddStickerCollection.FromString,
                    response_serializer=miscellaneous__pb2.ResponseSeq.SerializeToString,
            ),
            'RemoveStickerCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveStickerCollection,
                    request_deserializer=stickers__pb2.RequestRemoveStickerCollection.FromString,
                    response_serializer=miscellaneous__pb2.ResponseSeq.SerializeToString,
            ),
            'LoadStickerCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadStickerCollection,
                    request_deserializer=stickers__pb2.RequestLoadStickerCollection.FromString,
                    response_serializer=stickers__pb2.ResponseLoadStickerCollection.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.Stickers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Stickers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LoadOwnStickers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/LoadOwnStickers',
            stickers__pb2.RequestLoadOwnStickers.SerializeToString,
            stickers__pb2.ResponseLoadOwnStickers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadAcesssibleStickers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/LoadAcesssibleStickers',
            stickers__pb2.RequestLoadAcesssibleStickers.SerializeToString,
            stickers__pb2.ResponseLoadAcesssibleStickers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddStickerPackReference(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/AddStickerPackReference',
            stickers__pb2.RequestAddStickerPackReference.SerializeToString,
            miscellaneous__pb2.ResponseSeq.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveStickerPackReference(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/RemoveStickerPackReference',
            stickers__pb2.RequestRemoveStickerPackReference.SerializeToString,
            miscellaneous__pb2.ResponseSeq.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddStickerCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/AddStickerCollection',
            stickers__pb2.RequestAddStickerCollection.SerializeToString,
            miscellaneous__pb2.ResponseSeq.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveStickerCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/RemoveStickerCollection',
            stickers__pb2.RequestRemoveStickerCollection.SerializeToString,
            miscellaneous__pb2.ResponseSeq.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadStickerCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Stickers/LoadStickerCollection',
            stickers__pb2.RequestLoadStickerCollection.SerializeToString,
            stickers__pb2.ResponseLoadStickerCollection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
