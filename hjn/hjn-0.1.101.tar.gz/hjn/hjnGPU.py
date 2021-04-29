from gpuinfo import GPUInfo

def findGPU():
    """get ID of GPUS
    :param num_gpu:  num of GPUs to use
    :return: gpu_id: ID of allocated GPUs
    """
    gpu_id = None
    available_device=GPUInfo.check_empty()
    if not available_device is None:
        if len(available_device)>0:
            gpu_id=available_device[0]

    return gpu_id


