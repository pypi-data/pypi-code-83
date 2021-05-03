import time
import cv2
import numpy
from scipy.spatial import distance as dist
from faceservice.lib.core.api.facer import FaceAna



class Analyzer:
    def __init__(self):
        self.facer = FaceAna()
        self.n = 0


    def get_pos68(self,image):
        '''
        · 口可以访问 [48，68] 。
        · 右眉可以访问 [17，22]。
        · 左眉可以访问 [22，27] 。
        · 右眼可以访问 [36，42]。
        · 左眼 可以访问 [42，48]。
        · 鼻可以访问 [27，35]。  34是鼻尖
        · 下巴边框可以访问 [0，17]
        '''
        #self.image = cv2.imread(image_path)
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            start = time.time()
            boxes, landmarks, states = self.facer.run(image)
            # no track
            self.facer.reset()
            duration = time.time() - start
            print('one iamge cost %f s' % (duration))
            for face_index in range(landmarks.shape[0]):
                pos_list = []
                for landmarks_index in range(landmarks[face_index].shape[0]):
                    x_y = landmarks[face_index][landmarks_index]
                    pos = (int(x_y[0]), int(x_y[1]))
                    pos_list.append(numpy.array(pos))
            return pos_list
        except:
            print('完毕')

    def get_nose(self,image):
        pos_list = self.get_pos68(image)
        print('鼻尖坐标： %s' % pos_list[34])
        return pos_list[34]

    def get_eye(self, image):
        '''
        @param: image = cv2.imread(image_loc)
        '''
        # global n

        # pattern = np.zeros_like(image)
        # img_show = self.image.copy()
        pos_list = self.get_pos68(image)

        # 利用cv2.putText输出1-68
        # 各参数依次是：图片，添加的文字，坐标，字体，字体大小，颜色，字体粗细
        # cv2.putText(img_show, str(landmarks_index + 1), pos, font, 0.2, (0, 0, 255), 1, cv2.LINE_AA)
        # cv2.imwrite("./figure/" + "video%s.jpg" % str(n), img_show)
        # 右眼六个坐标
        right_eye = pos_list[36: 42]
        # 左眼六个坐标
        left_eye = pos_list[42:48]
        self.n += 1
        print('眼睛坐标：左 %s 右 %s' % (left_eye,right_eye))
        return left_eye, right_eye


class Action:
    NOD_THRESH = 200
    #需要调整
    NOSE_X_THRESH = 300
    NOSE_SHAKE_FRAMES = 1
    # 人眼纵横比参数
    EYE_AR_THRESH = 0.3  # 可以根据不同的人眼大小调整
    EYE_AR_CONSEC_FRAMES = 10  # 当监测到人眼超过50帧还在闭眼状态，说明人正在瞌睡

    # 检测帧次数
    COUNTER = 0
    n = 0
    analyzer = Analyzer()

    def eye_aspect_ratio(self, eye):
        return (dist.euclidean(eye[1], eye[5]) + dist.euclidean(eye[2], eye[4])) / (2.0 * dist.euclidean(eye[0], eye[3]))

    def analyze_wrapper(func):

        def analyze_wrappered(self,video_capture):
            # 从摄像头中获取人脸
            # vs = VideoStream(src= 0 ).start()
            #video_capture = cv2.VideoCapture(video_path)
            while video_capture.isOpened():
                #ret, image = video_capture.read()
                func(self, video_capture)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            video_capture.release()
            cv2.destroyAllWindows()

        return analyze_wrappered


    '''
    @analyze_wrapper
    def test_wrapper(self,video_capture):
        #video_capture = cv2.VideoCapture(video_path)
        ret, image = video_capture.read()

        leftEye, rightEye = Action.analyzer.get_eye(image)
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # 平均左右眼的纵横比
        ear = (leftEAR + rightEAR) / 2.

        # added by jfu
        # 计算ear是否小于设置的值
        global COUNTER
        if ear < Action.EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= Action.EYE_AR_CONSEC_FRAMES:
                # 此处放置当人瞌睡时要处理的函数
                # 当人闭眼时，显示警告信息
                cv2.putText(image, 'SLEEPING!!! EAR: {:.2f}'.format(ear), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            COUNTER = 0
            cv2.putText(image, 'EAR: {:.2f}'.format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow('frame', image)
        '''


    def isShakeHead(self, video_path):
        '''
        @nose_list : 一段视频中鼻子的坐标
        '''
        #min = sys.maxsize
        max = 0
        COUNTER = 0
        flag = 0 # 0是右 1是左
        video_capture = cv2.VideoCapture(video_path)
        while video_capture.isOpened():
            ret, image = video_capture.read()
            current = Action.analyzer.get_nose(image)
            x = current[0]
            #获取一组鼻坐标的最大值和最小值
            if max == 0:
                max = x
                min = x
                first = x
                print('鼻尖中正位置： %s' % x)
            elif x > max:
                max = x
            elif x < min:
                min = x

            if max - min > Action.NOSE_X_THRESH:
                COUNTER += 1
                #if COUNTER >= Action.NOSE_SHAKE_FRAMES:
                    # 此处放置当人瞌睡时要处理的函数
                    # 当人闭眼时，显示警告信息
                cv2.putText(image, '{} SHAKE EAR: {:.2f}'.format(COUNTER, (max - min)), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                min = first
                max = first

            else:
                # COUNTER = 0
                cv2.putText(image, '{} SHAKE EAR: {:.2f}'.format(COUNTER, (max - min)), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow('frame', image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()




    def isNodeHead(self, video_path):
        '''
        @nose_list : 一段视频中鼻子的坐标
        '''
        #min = sys.maxsize
        max = 0
        COUNTER = 0
        flag = 0 # 0是右 1是左
        video_capture = cv2.VideoCapture(video_path)
        while video_capture.isOpened():
            ret, image = video_capture.read()
            current = Action.analyzer.get_nose(image)
            y = current[1]
            #获取一组鼻坐标的最大值和最小值
            if max == 0:
                max = y
                min = y
                first = y
                print('鼻尖中正位置： %s' % y)
            elif y > max:
                max = y
            elif y < min:
                min = y

            if max - min > Action.NOD_THRESH:
                COUNTER += 1
                #if COUNTER >= Action.NOSE_SHAKE_FRAMES:
                # 此处放置当人瞌睡时要处理的函数
                # 当人闭眼时，显示警告信息
                cv2.putText(image, '{} NOD EAR: {:.2f}'.format(COUNTER, (max - min)), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                min = first
                max = first

            else:
                # COUNTER = 0
                cv2.putText(image, '{} NOD EAR: {:.2f}'.format(COUNTER, (max - min)), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow('frame', image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def isCloseEye(self,video_path):
        # 从摄像头中获取人脸
        # vs = VideoStream(src= 0 ).start()
        #video_capture = cv2.VideoCapture(video_path_or_cam)
        # 从摄像头中获取人脸
        # vs = VideoStream(src= 0 ).start()
        video_capture = cv2.VideoCapture(video_path)
        analyzer = Analyzer()

        while video_capture.isOpened():

            ret, image = video_capture.read()
            leftEye, rightEye = analyzer.get_eye(image)
            leftEAR = self.eye_aspect_ratio(leftEye)
            rightEAR = self.eye_aspect_ratio(rightEye)

            # 平均左右眼的纵横比
            ear = (leftEAR + rightEAR) / 2.

            # added by jfu
            # 计算ear是否小于设置的值
            global COUNTER
            if ear < self.EYE_AR_THRESH:
                COUNTER += 1
                if COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    # 此处放置当人瞌睡时要处理的函数
                    # 当人闭眼时，显示警告信息
                    cv2.putText(image, 'SLEEPING!!! EAR: {:.2f}'.format(ear), (300, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            else:
                COUNTER = 0
                cv2.putText(image, 'EAR: {:.2f}'.format(ear), (300, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow('frame', image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()













