# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from toit.api import program_pb2 as toit_dot_api_dot_program__pb2


class ProgramServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Run = channel.stream_stream(
                '/toit.api.ProgramService/Run',
                request_serializer=toit_dot_api_dot_program__pb2.RunRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.RunResponse.FromString,
                )
        self.RunStart = channel.unary_stream(
                '/toit.api.ProgramService/RunStart',
                request_serializer=toit_dot_api_dot_program__pb2.RunStartRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.RunResponse.FromString,
                )
        self.Compile = channel.unary_unary(
                '/toit.api.ProgramService/Compile',
                request_serializer=toit_dot_api_dot_program__pb2.CompileRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.CompileResponse.FromString,
                )
        self.Analyze = channel.unary_unary(
                '/toit.api.ProgramService/Analyze',
                request_serializer=toit_dot_api_dot_program__pb2.AnalyzeRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.AnalyzeResponse.FromString,
                )
        self.SyntaxAnalyze = channel.unary_unary(
                '/toit.api.ProgramService/SyntaxAnalyze',
                request_serializer=toit_dot_api_dot_program__pb2.SyntaxAnalyzeRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.SyntaxAnalyzeResponse.FromString,
                )
        self.LspAnalyze = channel.stream_stream(
                '/toit.api.ProgramService/LspAnalyze',
                request_serializer=toit_dot_api_dot_program__pb2.LspRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.LspResponse.FromString,
                )
        self.GetProgram = channel.unary_unary(
                '/toit.api.ProgramService/GetProgram',
                request_serializer=toit_dot_api_dot_program__pb2.GetProgramRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.GetProgramResponse.FromString,
                )
        self.GetCompilation = channel.unary_unary(
                '/toit.api.ProgramService/GetCompilation',
                request_serializer=toit_dot_api_dot_program__pb2.GetCompilationRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.GetCompilationResponse.FromString,
                )
        self.LookupPrograms = channel.unary_unary(
                '/toit.api.ProgramService/LookupPrograms',
                request_serializer=toit_dot_api_dot_program__pb2.LookupProgramsRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.LookupProgramsResponse.FromString,
                )
        self.DeviceRun = channel.unary_stream(
                '/toit.api.ProgramService/DeviceRun',
                request_serializer=toit_dot_api_dot_program__pb2.DeviceRunRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.DeviceRunResponse.FromString,
                )
        self.DecodeSystemMessage = channel.unary_unary(
                '/toit.api.ProgramService/DecodeSystemMessage',
                request_serializer=toit_dot_api_dot_program__pb2.DecodeSystemMessageRequest.SerializeToString,
                response_deserializer=toit_dot_api_dot_program__pb2.DecodeSystemMessageResponse.FromString,
                )


class ProgramServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Run(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunStart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Compile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Analyze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyntaxAnalyze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LspAnalyze(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProgram(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCompilation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupPrograms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeviceRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DecodeSystemMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProgramServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Run': grpc.stream_stream_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=toit_dot_api_dot_program__pb2.RunRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.RunResponse.SerializeToString,
            ),
            'RunStart': grpc.unary_stream_rpc_method_handler(
                    servicer.RunStart,
                    request_deserializer=toit_dot_api_dot_program__pb2.RunStartRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.RunResponse.SerializeToString,
            ),
            'Compile': grpc.unary_unary_rpc_method_handler(
                    servicer.Compile,
                    request_deserializer=toit_dot_api_dot_program__pb2.CompileRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.CompileResponse.SerializeToString,
            ),
            'Analyze': grpc.unary_unary_rpc_method_handler(
                    servicer.Analyze,
                    request_deserializer=toit_dot_api_dot_program__pb2.AnalyzeRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.AnalyzeResponse.SerializeToString,
            ),
            'SyntaxAnalyze': grpc.unary_unary_rpc_method_handler(
                    servicer.SyntaxAnalyze,
                    request_deserializer=toit_dot_api_dot_program__pb2.SyntaxAnalyzeRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.SyntaxAnalyzeResponse.SerializeToString,
            ),
            'LspAnalyze': grpc.stream_stream_rpc_method_handler(
                    servicer.LspAnalyze,
                    request_deserializer=toit_dot_api_dot_program__pb2.LspRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.LspResponse.SerializeToString,
            ),
            'GetProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProgram,
                    request_deserializer=toit_dot_api_dot_program__pb2.GetProgramRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.GetProgramResponse.SerializeToString,
            ),
            'GetCompilation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCompilation,
                    request_deserializer=toit_dot_api_dot_program__pb2.GetCompilationRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.GetCompilationResponse.SerializeToString,
            ),
            'LookupPrograms': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupPrograms,
                    request_deserializer=toit_dot_api_dot_program__pb2.LookupProgramsRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.LookupProgramsResponse.SerializeToString,
            ),
            'DeviceRun': grpc.unary_stream_rpc_method_handler(
                    servicer.DeviceRun,
                    request_deserializer=toit_dot_api_dot_program__pb2.DeviceRunRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.DeviceRunResponse.SerializeToString,
            ),
            'DecodeSystemMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.DecodeSystemMessage,
                    request_deserializer=toit_dot_api_dot_program__pb2.DecodeSystemMessageRequest.FromString,
                    response_serializer=toit_dot_api_dot_program__pb2.DecodeSystemMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'toit.api.ProgramService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProgramService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Run(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/toit.api.ProgramService/Run',
            toit_dot_api_dot_program__pb2.RunRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.RunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunStart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/toit.api.ProgramService/RunStart',
            toit_dot_api_dot_program__pb2.RunStartRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.RunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Compile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/Compile',
            toit_dot_api_dot_program__pb2.CompileRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.CompileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Analyze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/Analyze',
            toit_dot_api_dot_program__pb2.AnalyzeRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.AnalyzeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyntaxAnalyze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/SyntaxAnalyze',
            toit_dot_api_dot_program__pb2.SyntaxAnalyzeRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.SyntaxAnalyzeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LspAnalyze(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/toit.api.ProgramService/LspAnalyze',
            toit_dot_api_dot_program__pb2.LspRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.LspResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/GetProgram',
            toit_dot_api_dot_program__pb2.GetProgramRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.GetProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCompilation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/GetCompilation',
            toit_dot_api_dot_program__pb2.GetCompilationRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.GetCompilationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupPrograms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/LookupPrograms',
            toit_dot_api_dot_program__pb2.LookupProgramsRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.LookupProgramsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeviceRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/toit.api.ProgramService/DeviceRun',
            toit_dot_api_dot_program__pb2.DeviceRunRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.DeviceRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DecodeSystemMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toit.api.ProgramService/DecodeSystemMessage',
            toit_dot_api_dot_program__pb2.DecodeSystemMessageRequest.SerializeToString,
            toit_dot_api_dot_program__pb2.DecodeSystemMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
