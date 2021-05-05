import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
from sklearn.cluster import KMeans
from PIL import Image
import sys
import os
import time
import mimetypes


class Tat:
    def __init__(self, input_folder: str, output_folder: str):
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        self.input_folder = input_folder
        self.output_folder = output_folder

    @staticmethod
    def guess_type(filename):
        filetype = mimetypes.guess_type(filename)[0]
        if filetype is None:
            return None
        return filetype.split("/")[0]

    @staticmethod
    def is_image(filename):
        return Tat.guess_type(filename) == "image"

    @staticmethod
    def generate_layers(src_image: np.ndarray, cluster_count: int, run_count: int, max_iter_count: int):
        img_shape = src_image.shape
        start_time = time.time()
        k_means = KMeans(n_clusters=cluster_count, random_state=0, n_init=run_count, max_iter=max_iter_count).fit(
            filters.gaussian(src_image.reshape(img_shape[0] * img_shape[1], 1), 2))
        delta = time.time() - start_time
        print(f"k-means computing time: {delta}")
        segments = k_means.labels_.reshape(img_shape)
        labeled_segments = k_means.cluster_centers_[segments][:, :, 0]
        labeled_cluster = np.asarray(k_means.cluster_centers_)

        powers = np.floor(np.log10(labeled_segments))
        monochrome_labeled_segments = 100 ** powers * np.floor(labeled_segments / 100 ** powers)

        powers_cluster = np.floor(np.log10(labeled_cluster))
        monochrome_labeled_cluster = np.sort(100 ** powers_cluster * np.floor(labeled_cluster / 100 ** powers_cluster),
                                             axis=0)

        layers = []
        for i in range(len(monochrome_labeled_cluster)):
            layer = np.zeros(shape=np.shape(monochrome_labeled_segments)).astype(np.uint8)
            layer[monochrome_labeled_segments == monochrome_labeled_cluster[i]] = 1
            layers.append(layer)
        return layers, monochrome_labeled_segments

    def generate(self, cluster_count: int, run_count: int, max_iter_count: int):
        for entry in os.scandir(self.input_folder):
            if not self.is_image(entry.path):
                continue

            image = Image.open(entry.path)
            input_basename = (lambda basename: basename[0:basename.rfind(".")])(os.path.basename(entry.path))

            layers = self.generate_layers(np.asarray(image), cluster_count, run_count, max_iter_count)
            for i in range(len(layers)):
                layer = layers[i]
                plt.imshow(layer)
                plt.savefig(os.path.join(self.output_folder, f"{input_basename}_layer_{i}.png"))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input dir> <output dir>")
        exit(1)
    tat = Tat(sys.argv[1], sys.argv[2])
    tat.generate(4, 50, 1000)
