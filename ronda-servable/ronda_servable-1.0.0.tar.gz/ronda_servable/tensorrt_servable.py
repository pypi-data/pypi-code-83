import logging
import os
from typing import Dict

import numpy as np

from .device_util import GPU_DEVICE, DEFAULT_FP16_VALUE, DEFAULT_WORKSPACE_VALUE, DEFAULT_BATCH_SIZE


class HostDeviceMem(object):
    def __init__(self, host_mem, device_mem):
        """Within this context, host_mom means the cpu memory and device means the GPU memory
        """
        self.host = host_mem
        self.device = device_mem

    def __str__(self):
        return "Host:\n" + str(self.host) + "\nDevice:\n" + str(self.device)

    def __repr__(self):
        return self.__str__()


class TensorRTServable:
    def __init__(self, local_path: str):
        self.local_path = local_path
        self.model_ins = None
        self.model_init_stat = False
        self.device = GPU_DEVICE

        self.fp16 = DEFAULT_FP16_VALUE
        self.workspace = DEFAULT_WORKSPACE_VALUE
        self.max_batch_size = DEFAULT_BATCH_SIZE

        self.optim_batch_size = self.max_batch_size

        self.model_input_list = None
        self.model_output_list = None

        self.engine_file = self.local_path + ".engine"
        self.trt_logger = None
        self.engine = None
        self.context = None
        self.bindings = None
        self.input_bindings = None
        self.output_bindings = None
        self.binding_idx = None
        self.stream = None

    def load(self):
        if self.model_init_stat:
            return

        import pycuda.driver as cuda
        import pycuda.autoinit  # pylint: disable=unused-import
        import tensorrt as trt

        self.trt_logger = trt.Logger(trt.Logger.Severity.INFO)

        if os.path.exists(self.engine_file):
            with open(self.engine_file, "rb") as f_engine, \
                    trt.Runtime(self.trt_logger) as runtime:

                self.engine = runtime.deserialize_cuda_engine(f_engine.read())
        else:
            network_creation_flag = 1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)

            with trt.Builder(self.trt_logger) as builder, \
                    builder.create_network(network_creation_flag) as network, \
                    trt.OnnxParser(network, self.trt_logger) as parser:

                builder.max_workspace_size = self.workspace
                builder.max_batch_size = 1
                builder.fp16_mode = self.fp16

                # parse onnx file
                with open(self.local_path, "rb") as f_onnx:
                    if not parser.parse(f_onnx.read()):
                        logging.error("onnx file parse error")
                        for i in range(parser.num_errors):
                            logging.error("error %d: %s", i, parser.get_error(i))

                        raise Exception("onnx file parse error")

                # set dynamic batch size
                builder_config = builder.create_builder_config()
                builder_config.max_workspace_size = self.workspace

                if self.fp16:
                    builder_config.flags = 1 << trt.BuilderFlag.FP16

                profile = builder.create_optimization_profile()
                for i in range(network.num_inputs):
                    input_name = network.get_input(i).name
                    input_shape = list(network.get_input(i).shape)
                    min_shape = input_shape.copy()
                    min_shape[0] = 1
                    optim_shape = input_shape.copy()
                    optim_shape[0] = self.optim_batch_size
                    max_shape = input_shape.copy()
                    max_shape[0] = self.max_batch_size
                    profile.set_shape(input_name, min_shape, optim_shape, max_shape)

                builder_config.add_optimization_profile(profile)
                self.engine = builder.build_engine(network, config=builder_config)

                with open(self.engine_file, "wb") as f_engine:
                    f_engine.write(self.engine.serialize())

        self.context = self.engine.create_execution_context()

        # allocate buffers
        self.model_input_list = []
        self.model_output_list = []
        self.input_bindings = {}
        self.output_bindings = {}
        self.bindings = []
        self.binding_idx = {}

        for i, binding in enumerate(self.engine):
            max_shape = list(self.engine.get_binding_shape(binding))
            max_shape[0] = self.max_batch_size
            size = trt.volume(max_shape)
            dtype = trt.nptype(self.engine.get_binding_dtype(binding))
            # Allocate host and device buffers
            host_mem = cuda.pagelocked_empty(size, dtype)
            device_mem = cuda.mem_alloc(host_mem.nbytes)
            # Append the device buffer to device bindings.
            self.bindings.append(int(device_mem))
            # Append to the appropriate list.
            if self.engine.binding_is_input(binding):
                self.input_bindings[binding] = HostDeviceMem(host_mem, device_mem)
                self.model_input_list.append(binding)
            else:
                self.output_bindings[binding] = HostDeviceMem(host_mem, device_mem)
                self.model_output_list.append(binding)

            self.binding_idx[binding] = i

        self.stream = cuda.Stream()

    def forward(self, inputs: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        import pycuda.driver as cuda
        import tensorrt as trt

        input_dict = {}
        for key in self.model_input_list:
            if key not in inputs:
                raise Exception("necessary input (%s) missing and model needs %s" % (key, self.model_input_list))
            input_dict[key] = inputs[key]

        batch_size = next(iter(inputs.values())).shape[0]

        # set input binding shape
        for input_name, arr in inputs.items():
            self.context.set_binding_shape(self.binding_idx[input_name], arr.shape)

        # transfer data to GPU
        for input_name, arr in inputs.items():
            np.copyto(self.input_bindings[input_name].host[:arr.size], np.ravel(arr))
            cuda.memcpy_htod_async(self.input_bindings[input_name].device,
                                   self.input_bindings[input_name].host[:arr.size],
                                   stream=self.stream)

        # inference
        self.context.execute_async_v2(self.bindings, self.stream.handle)

        # transfer data back to CPU
        for output_name, binding in self.output_bindings.items():
            shape = list(self.engine.get_binding_shape(output_name))
            shape[0] = batch_size

            size = trt.volume(shape)
            cuda.memcpy_dtoh_async(binding.host[:size], binding.device, stream=self.stream)

        self.stream.synchronize()

        output_dict = {}
        for output_name in self.model_output_list:
            shape = list(self.engine.get_binding_shape(output_name))
            shape[0] = batch_size

            size = trt.volume(shape)
            arr = self.output_bindings[output_name].host[:size].copy()
            arr = np.reshape(arr, shape)
            output_dict[output_name] = arr

        return output_dict