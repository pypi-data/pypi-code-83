import cv2
import time

import numpy
import numpy as np
import os



from faceservice.lib.core.api.facer import FaceAna
from faceservice.lib.core.headpose.pose import get_head_pose, line_pairs
from faceservice.lib.web.http import app

from config import config as cfg

# 人眼纵横比参数
EYE_AR_THRESH = 0.3 #可以根据不同的人眼大小调整
EYE_AR_CONSEC_FRAMES = 50 # 当监测到人眼超过50帧还在闭眼状态，说明人正在瞌睡

#检测帧次数
COUNTER = 0

from scipy.spatial import distance as dist
def eye_aspect_ratio(eye):
    return (dist.euclidean(eye[1],eye[5]) + dist.euclidean(eye[2],eye[4]))/(2.0 * dist.euclidean(eye[0],eye[3]))

def get_eye_pos(image_loc):
    facer = FaceAna()

    image = cv2.imread(image_loc)

    pattern = np.zeros_like(image)

    img_show = image.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    start = time.time()
    boxes, landmarks, states = facer.run(image)

    ###no track
    facer.reset()

    duration = time.time() - start
    print('one iamge cost %f s' % (duration))

    for face_index in range(landmarks.shape[0]):


        pos_list = []
        for landmarks_index in range(landmarks[face_index].shape[0]):
            x_y = landmarks[face_index][landmarks_index]
            pos = (int(x_y[0]), int(x_y[1]))
            print(landmarks_index, pos)
            pos_list.append(numpy.array(pos))

            # 利用cv2.putText输出1-68
            font = cv2.FONT_HERSHEY_SIMPLEX
            # 各参数依次是：图片，添加的文字，坐标，字体，字体大小，颜色，字体粗细
            cv2.putText(img_show, str(landmarks_index + 1), pos, font, 0.2, (0, 0, 255), 1, cv2.LINE_AA)

    right_eye = pos_list[36: 42]
    left_eye = pos_list[42:48]
    print(right_eye)
    print(left_eye)
    return left_eye,right_eye

#加载人脸68点数据模型
detector = dlib.get_frontal_face_detector()
predictor =dlib.hape_predictor("shape_predictor_68_face_landmarks.dat")

#获取人眼的坐标
(lStart,lEnd) = face_utils.FACIAL_LANDMARKS_INDX["left_eye"]
(rStart,rEnd)  = face_utils.FACIAL_LANDMARKS_INDX["right_eye"]

#从摄像头中获取人脸
vs = VideoStream(src= 0 ).start()
time.sleep(3.)
while True:
    #从视频中获取图片来检测
    frame = vs.read()
    frame = imutils.resize(frame, width = 450)
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for rect in rects :
        shape = predictor(gray, rect)
        shhape = face_utils.shape

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        #平均左右眼的纵横比
        ear = (leftEAR + rightEAR ) / 2.
        #显示左右眼
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0,255,0),1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)


    #added by jfu
    #计算ear是否小于设置的值
    if ear < EYE_AR_THRESH:
        COUNTER +=1
        if COUNTER >=EYE_AR_CONSEC_FRAMES:
            #此处放置当人瞌睡时要处理的函数
            #当人闭眼时，显示警告信息
            cv2.putText(frame, '警告信息',(10,30), cv2.FONT_HERSHHEY_SHIMPLEX,0.7,(0,0,255),2)
        else:
            COUNTER = 0
            cv2.putText(frame, 'EAR: {:.2f}'.format(ear),(300,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    vs.stop()
