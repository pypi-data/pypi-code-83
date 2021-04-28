import os
import numpy as np


def create_slice_mesh(file_name,
                      centre_point=np.array([0, 0, 0]),
                      x_len=500e-6,
                      y_len=500e-6,
                      z_len=150e-6,
                      description=None):

    mesh_dir = os.path.dirname(file_name)
    if mesh_dir and not os.path.exists(mesh_dir):
        os.makedirs(mesh_dir)

    # 2019-11-26 : Anya said that her sagital striatal slices were 2.36 x 2.36 mm.
    #              so that can be an upper limit
    if type(centre_point) is not np.ndarray:
        centre_point = np.array(centre_point)

    print("Creating slice mesh")
    print(f"File: {file_name}")
    print(f"Centre: {centre_point}")
    print(f"Sides: {x_len} x {y_len} x {z_len}")
    print(f"Description: {description}")

    vertex = np.array([[0.0, 0.0, 0.0],
                       [0.0, 0.0, 1.0],
                       [0.0, 1.0, 0.0],
                       [0.0, 1.0, 1.0],
                       [1.0, 0.0, 0.0],
                       [1.0, 0.0, 1.0],
                       [1.0, 1.0, 0.0],
                       [1.0, 1.0, 1.0]])

    # Centre cube
    vertex -= np.array([0.5, 0.5, 0.5])

    # Scale the cube to right size
    vertex[:, 0] *= x_len
    vertex[:, 1] *= y_len
    vertex[:, 2] *= z_len

    # Position cube

    vertex += centre_point

    vertex *= 1e6  # The other obj files are in micrometers, so convert :(

    normal_str = "vn  0.0  0.0  1.0\n" \
                 + "vn  0.0  0.0 -1.0\n" \
                 + "vn  0.0  1.0  0.0\n" \
                 + "vn  0.0 -1.0  0.0\n" \
                 + "vn  1.0  0.0  0.0\n" \
                 + "vn -1.0  0.0  0.0\n"

    face_str = "f  1//2  7//2  5//2\n" \
               + "f  1//2  3//2  7//2\n" \
               + "f  1//6  4//6  3//6\n" \
               + "f  1//6  2//6  4//6\n" \
               + "f  3//3  8//3  7//3\n" \
               + "f  3//3  4//3  8//3\n" \
               + "f  5//5  7//5  8//5\n" \
               + "f  5//5  8//5  6//5\n" \
               + "f  1//4  5//4  6//4\n" \
               + "f  1//4  6//4  2//4\n" \
               + "f  2//1  6//1  8//1\n" \
               + "f  2//1  8//1  4//1\n"

    with open(file_name, 'wt') as f:
        f.write("# Generated by create_slice_mesh.py\n")
        f.write(f"# {description}\n\n")
        f.write("g cube\n\n")

        for row in vertex:
            f.write("v %f %f %f\n" % tuple(row))

        f.write(f"\n{normal_str}")
        f.write(f"\n{face_str}")


if __name__ == "__main__":
    create_slice_mesh(file_name="test-slice-alex.obj",
                      centre_point=[0.5, 0.5, 0.0],
                      x_len=1e-3,
                      y_len=1e-3,
                      z_len=25e-6,
                      description="This is a test slice for Alex")
