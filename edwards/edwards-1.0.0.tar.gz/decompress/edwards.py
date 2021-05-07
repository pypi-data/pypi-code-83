import os
import platform
from ctypes import cdll

curve25519_lib_name = "libcurve25519"
curve25519_lib_ex_name = ""
system_name = platform.system()
if system_name == "Darwin":
	curve25519_lib_ex_name = ".dylib"
elif system_name == "Windows":
	curve25519_lib_ex_name = ".dll"
elif system_name == "Linux":
	curve25519_lib_ex_name = ".so"
else:
	raise Exception("invalid system type")

BASE_DIR = os.path.dirname(__file__)
lib_path = os.path.join(BASE_DIR, f"{curve25519_lib_name + curve25519_lib_ex_name}")
curve25519_lib = cdll.LoadLibrary(lib_path)


# Attempt to decompress to an EdwardsPoint.
# Returns False if the input is not the \(y\)-coordinate of a curve point.
def decompress(sha3_256_hash: bytes) -> bool:
	res = curve25519_lib.decompress(sha3_256_hash)
	
	return res
