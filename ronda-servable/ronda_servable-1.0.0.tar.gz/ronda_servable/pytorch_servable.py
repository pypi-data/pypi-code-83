import logging

from .device_util import CPU_DEVICE, get_cpu_procs, get_gpu_available
from tml_serving.utils.torch_util import place_on_device, set_torch_num_threads

class PytorchServable:
    """
    pytorch servable 输入dict[str, ndarray]，输出dict[str, ndarray]
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
            import torch
            set_torch_num_threads()

            if get_gpu_available() and self.device != CPU_DEVICE:
                self.torch_device = torch.device(GPU_DEVICE)
            else:
                self.torch_device = torch.device(CPU_DEVICE)

            sys.path.append(os.path.dirname(self.local_path))
            self.model_ins = torch.load(self.local_path, map_location=self.torch_device)
            self.model_ins.eval()
            self.model_init_stat = True

    def forward(self, *args, **kwargs):
        import torch
        # 默认实现，torch模型返回值是tensor
        args = place_on_device(args, self.torch_device)
        kwargs = place_on_device(kwargs, self.torch_device)

        with torch.no_grad():
            if len(args) == 1 and isinstance(args[0], tuple):
                output = self.model_ins(*args[0], **kwargs)
            else:
                output = self.model_ins(*args, **kwargs)

            output = place_on_device(output, torch.device(CPU_DEVICE))
            return output