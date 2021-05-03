import cv2
import os
import math
import numpy as np

from ksl_util.file.image.image_loader import ImagePairHolder, PairLoader
from ksl_util.log import printlog


def miou(pred, anno):

    tp = np.logical_and(pred, anno)
    tp = np.asarray(tp, 'float64')
    tp = np.sum(tp)

    fp = np.logical_and(np.logical_not(anno), pred)
    fp = np.asarray(fp, 'float64')
    fp = np.sum(fp)

    fn = np.logical_and(np.logical_not(pred), anno)
    fn = np.asarray(fn, 'float64')
    fn = np.sum(fn)

    tn = np.logical_and(np.logical_not(pred), np.logical_not(anno))
    tn = np.asarray(tn, 'float64')
    tn = np.sum(tn)

    return tp, fp, fn, tn


def sensitivity(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TP / (TP + FN) if TP + FN != 0 else None


def specificity(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TN / (TN + FP) if TN + FP != 0 else None


def precision(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TP / (TP + FP) if TP + FP != 0 else None


def recall(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TP / (TP + FN) if TP + FN != 0 else None


def accuracy(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return (TP + TN) / (TP + TN + FP + FN) if TP + FN + FP + TN != 0 else 1.0


def ppv(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TP / (TP + FP) if TP + FN != 0 else None


def npv(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return TN / (TN + FN) if TN + FN != 0 else None


def f1_score(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return (TP + TP) / (TP + TP + FP + FN) if TP + FN + FP + TN != 0 else 1.0


def balanced_accuracy(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return (sensitivity(TP, FP, FN, TN) + specificity(TP, FP, FN, TN)) / 2.0


def MCC(TP, FP, FN, TN):
    TP, FP, FN, TN = tuple([float(p) for p in [TP, FP, FN, TN]])
    return (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) if (TP + FP) * (TP + FN) * (
            TN + FP) * (TN + FN) != 0 else None


def all_evaluations(TP, FP, FN, TN):
    results = dict()
    for func in [
        sensitivity, specificity, precision, recall, ppv, npv, f1_score, accuracy, balanced_accuracy, MCC
    ]:
        results[func.__name__] = func(TP, FP, FN, TN)
    return results



def save_evaluate(path_image, path_ground, absolute_file_name):

    num_images, num_ground = len(os.listdir(path_image)), len(os.listdir(path_ground))

    assert num_images == num_ground, 'Different number of images'

    loader = PairLoader()
    loader.load_path(path_image, path_ground)

    images = loader.load_images(num_images, grayscales=(True, True), printable=True, random=False)
    printlog('loaded!!')

    tTP = 0
    tFP = 0
    tFN = 0
    tTN = 0
    tmatched = 0
    index = 0

    with open(absolute_file_name, 'w') as save_file_name:
        printlog(save_file_name)
        save_file_name.write('index, iou, acc, TP, FP, FN, TN')
        save_file_name.write('\n')

        for image in images:
            img, gnd = image[0], image[1]
            matched, TP, FP, FN, TN = miou(img, gnd)

            TP += 1e-15
            tTP += TP
            tFP += FP
            tFN += FN
            tTN += TN
            tmatched += matched

            message = '%d, %05f, %05f, %d, %d, %d, %d\n' % (index, float(TP) / (TP + FP + FN), float(matched) / (TP + TN + FN + FP), TP, FP, FN, TN)
            save_file_name.write(message)
            index += 1

        message = '%s, %05f, %05f, %d, %d, %d, %d\n' % ('mean', float(tTP) / (tTP + tFP + tFN), float(tmatched) / (tTP + tTN + tFN + tFP), tTP, tFP, tFN, tTN)
        printlog(message)
        save_file_name.write(message)

    print('fin.\n\n')
