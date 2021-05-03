import numpy as np
import cv2

def cal_IoU(img, gnd):
    img = img > 0
    gnd = gnd > 0
    
    tp = np.logical_and(img, gnd)
    fp = np.logical_and(np.logical_not(gnd), img)
    fn = np.logical_and(gnd, np.logical_not(img))
    tn = np.logical_and(np.logical_not(img), np.logical_not(gnd))
    
    tp = tp.astype(np.float32)
    fp = fp.astype(np.float32)
    fn = fn.astype(np.float32)
    tn = tn.astype(np.float32)
    
    tp = np.sum(tp)
    fp = np.sum(fp)
    fn = np.sum(fn)
    tn = np.sum(tn)
    
    iou = tp / (tp + fp + fn) if tp + fp + fn != 0 else 1.0
    
    return iou, tp, fp, fn, tn



if __name__ == '__main__':


    path_img = 'N:\\SPIE\\prediction_paper\\Fluo-N2DL-HeLa\\FusionNet_batch=1_size=384'
    path_gnd = 'R:\\Resource\\Fluo-N2DL-HeLa\\training_images2\\gnd'
    
    img = cv2.imread('%s/0000.png' % path_img)
    gnd = cv2.imread('%s/01_t013.png' % path_gnd)

    print(cal_IoU(img, gnd))
