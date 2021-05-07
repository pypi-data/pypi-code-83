GPU_DEVICE = "cuda"
CPU_DEVICE = "cpu"

DEFAULT_FP16_VALUE = False
DEFAULT_WORKSPACE_VALUE = 12 * 1 << 30  # 12GB
DEFAULT_BATCH_SIZE = 4


def get_cpu_procs():
    import automaxprocs
    available_procs = automaxprocs.cpu_count()
    max_procs = automaxprocs.get_max_procs()
    if max_procs != -1:
        available_procs = max_procs
    return available_procs


def get_gpu_available():
    import pynvml
    try:
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()
        return device_count > 0
    except:  # pylint: disable=bare-except
        return False
