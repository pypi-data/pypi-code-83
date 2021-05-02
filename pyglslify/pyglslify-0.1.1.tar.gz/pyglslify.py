import subprocess
import sys


def glslify(shader_path, *transforms):
    args = ["glslify", shader_path]
    if transforms:
        args.append("-t")
        args.extend(transforms)
    return subprocess.check_output(args, encoding=sys.getdefaultencoding())


if __name__ == "__main__":
    shader = glslify(sys.argv[1], *sys.argv[2:])
    print(shader)
