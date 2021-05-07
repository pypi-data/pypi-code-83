import logging
from typing import Dict

import numpy as np

from .device_util import CPU_DEVICE, get_cpu_procs, get_gpu_available

PROVIDER_LIST = ["TensorrtExecutionProvider", "CUDAExecutionProvider",
                 "OpenVINOExecutionProvider", "CPUExecutionProvider"]


class ONNXServable:
    """
    onnx servable 输入dict[str, ndarray]，输出dict[str, ndarray]
    """

    def __init__(self, local_path: str):
        self.local_path = local_path
        self.model_ins = None
        self.model_init_stat = False

        self.device = CPU_DEVICE
        self.provider_key = None

        self.model_input_list = None
        self.model_output_list = None

    def load(self):
        if not self.model_init_stat:
            import onnxruntime
            logging.info("onnxruntime current device: %s, available execution providers: %s",
                         onnxruntime.get_device(), str(onnxruntime.get_available_providers()))

            options = onnxruntime.SessionOptions()
            options.execution_mode = onnxruntime.ExecutionMode.ORT_SEQUENTIAL
            options.inter_op_num_threads = 1
            options.intra_op_num_threads = get_cpu_procs()
            options.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL

            if self.provider_key is None:
                providers = onnxruntime.get_available_providers()
            else:
                providers = self.provider_key.copy()

            if not get_gpu_available() or self.device == CPU_DEVICE:
                if "CUDAExecutionProvider" in providers:
                    providers.remove("CUDAExecutionProvider")
                if "TensorrtExecutionProvider" in providers:
                    providers.remove("TensorrtExecutionProvider")

            ordered_providers = []
            for provider in PROVIDER_LIST:
                if provider in providers:
                    ordered_providers.append(provider)
            logging.info("use execution providers: %s", str(ordered_providers))

            self.model_ins = onnxruntime.InferenceSession(self.local_path, options, providers=ordered_providers)
            self.model_init_stat = True

            self.model_input_list = []
            for input_obj in self.model_ins.get_inputs():
                self.model_input_list.append(input_obj.name)
                logging.info("model input name: %s shape: %s", input_obj.name, input_obj.shape)

            self.model_output_list = []
            for output_obj in self.model_ins.get_outputs():
                self.model_output_list.append(output_obj.name)
                logging.info("model output name: %s shape: %s", output_obj.name, output_obj.shape)

    def forward(self, inputs: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        if not isinstance(inputs, dict):
            raise Exception("onnx servable can only support dict input, got (%s) type" % type(inputs))

        input_dict = {}
        for key in self.model_input_list:
            if key not in inputs:
                raise Exception("necessary input (%s) missing and model needs %s" % (key, self.model_input_list))
            input_dict[key] = inputs[key]

        output_list = self.model_ins.run(None, input_dict)
        output_dict = {}
        for i, key in enumerate(self.model_output_list):
            output_dict[key] = output_list[i]

        return output_dict
