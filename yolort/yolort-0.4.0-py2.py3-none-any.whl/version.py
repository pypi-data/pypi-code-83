__version__ = '0.4.0'
git_version = '28ead0b1d369f85aa2bf0c8aa4b7aafd9a331443'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
