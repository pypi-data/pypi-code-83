# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import obsolete_pb2 as obsolete__pb2


class ObsoleteStub(object):
    """/ deprecated
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Obsolete = channel.unary_unary(
                '/dialog.Obsolete/Obsolete',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
                )
        self.SeqUpdates = channel.unary_stream(
                '/dialog.Obsolete/SeqUpdates',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=obsolete__pb2.ObsoleteSeqUpdateBox.FromString,
                )
        self.WeakUpdates = channel.stream_stream(
                '/dialog.Obsolete/WeakUpdates',
                request_serializer=obsolete__pb2.ObsoleteWeakUpdateCommand.SerializeToString,
                response_deserializer=obsolete__pb2.ObsoleteWeakUpdateBox.FromString,
                )


class ObsoleteServicer(object):
    """/ deprecated
    """

    def Obsolete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SeqUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WeakUpdates(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObsoleteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Obsolete': grpc.unary_unary_rpc_method_handler(
                    servicer.Obsolete,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
            ),
            'SeqUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.SeqUpdates,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=obsolete__pb2.ObsoleteSeqUpdateBox.SerializeToString,
            ),
            'WeakUpdates': grpc.stream_stream_rpc_method_handler(
                    servicer.WeakUpdates,
                    request_deserializer=obsolete__pb2.ObsoleteWeakUpdateCommand.FromString,
                    response_serializer=obsolete__pb2.ObsoleteWeakUpdateBox.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.Obsolete', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Obsolete(object):
    """/ deprecated
    """

    @staticmethod
    def Obsolete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Obsolete/Obsolete',
            google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SeqUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dialog.Obsolete/SeqUpdates',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            obsolete__pb2.ObsoleteSeqUpdateBox.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WeakUpdates(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/dialog.Obsolete/WeakUpdates',
            obsolete__pb2.ObsoleteWeakUpdateCommand.SerializeToString,
            obsolete__pb2.ObsoleteWeakUpdateBox.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
