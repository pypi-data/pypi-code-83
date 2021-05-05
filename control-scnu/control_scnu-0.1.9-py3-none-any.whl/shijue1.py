import numpy as np
import cv2
import imutils
import pyzbar.pyzbar as pyzbar
# 安装pyzbar：pip3 install pyzbar
from collections import deque

main_path = '/home/pi/class/'  # 读取和保存文件所用主文件夹
picture_path = main_path+'picture/'  # 图片文件夹
model_path = main_path+'model/'  # 识别模型文件夹
d_path = main_path + 'camera_pos/'

items_num= {0: '9', 1: '1', 2: '2', 3: '3',4: '4', 5: '5',6: '6', 7: '7',8: '8'}  #方向数字指示牌
items_dir={9: '左转', 10: '右转'}
items_label={11: '语音'}
items_laji = {0: '易拉罐', 1: '纸团', 2: '塑料瓶', 3: '电池',4: '报纸', 5: '灯泡',6: '花生壳', 7: '香蕉皮'}


class Assist_converse:
    def __init__(self):
        pass
    

def pic_read(path):
    img=cv2.imread(path)
    return img


class Camera():
    def __init__(self,num=0):
        self.img=[]
        self.cam = cv2.VideoCapture(num)
    def read_camera(self):
        self.ret, self.img = self.cam.read()
        if self.ret:
            return self.img
        else:
            print("未检测到摄像头，请注意摄像头是否接触不良或者未设置允许摄像头")
    def close_camera(self):
        self.cam.release()

# #赋值a为0号摄像头
# a=Camera(0)
#
# #关闭a摄像头
# #a.close_camera()
#
# #img为从a摄像头获取图像
# img=Img(a.read_camera())

#img为从" "读取图像
#img=Img(pic_read(" "))
        
#img定义窗口" "
#img.name_windows(" ")

#img在窗口" "展示图片
#img.show_image(" ")

#img设置窗口延时为time毫秒
#img.delay(time)

#img修改图片大小为0x0像素
#img.resize((0,0))

#img提取hsv颜色变为二值化图
#img.extract_color(hsv_low,hsv_top)

#img二值化图进行腐蚀操作
#img.erosion()

#img二值化图进行膨胀操作
#img.dilation()

#img二值化图计算偏移量(有返回值)
#img.offset_calculate1()

#img二值化图判断线路角度(有返回值)
#img.line_angle1()

#img二值化图是否有线路(有返回值)
#img.offset1()

#img二值化图是否虚线(有返回值)
#img.dotted_line1()



#img判断轮廓c包围的面积（有返回值）
#img.cnt_area(c)

#img获得二值化图所有轮廓（有返回值）
#img.bin_detect(c)

#img框选轮廓c标注文字shape
#img.cnt_draw(c,shape)

#img彩色图计算偏移量(有返回值)
#img.offset_calculate2()

#img彩色图判断线路角度(有返回值)
#img.line_angle2()

#img彩色图是否有线路(有返回值)
#img.offset2()

#img彩色图是否虚线(有返回值)
#img.dotted_line2()

#img当前图像类型（有返回值）
#img.Type

#img彩色图变为灰度图
#img.BGR2GRAY()

#img灰度图变为二值化图
#img.GRAY2BIN()

#img判断轮廓c是否"圆形"形状（有返回值,"圆形"为可选变量"三角形"，"四边形","五边形"）
#img.detect(c,"圆形")
        
#img关闭所有窗口
#img.close_windows()
        
#img保存图片到路径“”
#img.write_image("")


class Img(Assist_converse):
    def __init__(self,img=[]):
        self.img=img
        self.time=40
        self.flag_mask = 0
        self.flag_cap = 0
        self.Type="彩色图"
        
    def name_windows(self,name):
        cv2.namedWindow(name,0)
        
    def close_windows(self):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        
    def show_image(self,windows_name):
        cv2.resizeWindow(windows_name,640,480)
        cv2.imshow(windows_name,self.img)
        cv2.waitKey(self.time)
        
    def write_image(self,path):
        cv2.imwrite(path,self.img)
        
    def delay(self,time):
        self.time=time
        
    def resize(self,newsize=(1,1)):
        self.img=cv2.resize(self.img,newsize)
        
    def extract_color(self,lower_hsv,upper_hsv): 
        image_HSV=cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        lower_hsv=np.array(lower_hsv)
        upper_hsv=np.array(upper_hsv)
        self.img=cv2.inRange(self.img,lower_hsv,upper_hsv)
        self.Type="二值化图"
        
    def erosion(self):
        self.img = cv2.erode(self.img, None, iterations=2)
        
    def dilation(self):
        self.img = cv2.dilate(self.img, None, iterations=2)
        
    def BGR2GRAY(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.Type="灰度图"
        
    def GRAY2BIN(self):
        _, self.img = cv2.threshold(self.img, 0, 255, cv2.THRESH_OTSU)
        self.Type="二值化图"
        
    #二值化图寻迹
    def offset_calculate1(self,y=-1,img=[]):
        if len(img)==0:
            img=self.img
        if -1==y:
            y=img.shape[0]
            y=y//2
        line = img[y]
        white_count = np.sum(line == 0)
        white_index = np.where(line == 0)
        if white_count == 0:
            return 0
        center = (white_index[0][white_count - 1] + white_index[0][0]) / 2
        #求图像中心
        img_width=self.img.shape[1]
        img_center=img_width//2
        direction = center - img_center
        direction=int(direction)
        return direction
    
    def line_angle1(self,img=[]):
        if len(img)==0:
            img=self.img
        h=img.shape[0]
        up=[]
        down=[]
        for i in range(0,h//2,10):
            up.append(self.offset_calculate1(i))
        for i in range(h//2,h,10):
            down.append(self.offset_calculate1(i))
        a=sum(up)//len(up)
        b=sum(down)//len(down)
        angle=(a-b)//180
        return angle
    
    def offset1(self,img=[]):
        if len(img)==0:
            img=self.img
        y=img.shape[0]
        line =img[y//2]
        white_count = np.sum(line == 0)
        white_index = np.where(line == 0)
        if white_count == 0:
            return False
        else:
            return True
        
    def dotted_line1(self,img=[]):
        if len(img)==0:
            img=self.img
        cnts=self.bin_detect(img)
        x=[]
        for c in cnts:
            area=self.cnt_area(c)
            M=cv2.moments(c)
            if area>3000:
                cx=int(M["m10"]/M["m00"])
                x.append(cx)
        if len(x)<2:
            return False
        a=np.std(np.array(x))
        if a>150:
            return False
        else:
            return True
    #彩色图寻迹
    
    def offset_calculate2(self):
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)
        retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        img = cv2.dilate(dst, None, iterations=2)
        h=img.shape[0]
        direction=self.offset_calculate1(h//2,img)
        return direction
    
    def line_angle2(self):
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)
        retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        img = cv2.dilate(dst, None, iterations=2)
        angele=self.line_angle1(img)
        return angele
    
    def offset2(self):
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)
        retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        img= cv2.dilate(dst, None, iterations=2)
        result=self.offset1(img)
        return result
    
    def dotted_line2(self):
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)
        retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        img = cv2.dilate(dst, None, iterations=2)
        result=self.dotted_line1(img)
        return result
    
    def cnt_area(self,cnt):
        area=cv2.contourArea(cnt)
        return area
    
    def detect(self,c,Shape):
        #定义形状名称和判断近似形状
        shape = "未知形状"
        peri = cv2.arcLength(c, True)#周长
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        r1=peri/6.2#半径
        area=cv2.contourArea(c)#面积
        r2=(area/3.14)**0.5
        if abs(r1-r2)<0.22*r1 and len(approx)>4:
            shape="圆形"
        elif len(approx) == 3:
            shape = "三角形"
        #判断四边形是正方形还是长方形
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "正方形" if ar >= 0.95 and ar <= 1.05 else "长方形"
        else:
            pass
        return (shape==Shape)

    def bin_detect(self,img=[]):
        if len(img)==0:
            img=self.img
        # 在阈值图像中查找轮廓并初始化形状检测器
        cnts = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(cnts)
        max_cnts=[]
        for c in cnts:
            area=self.cnt_area(c)
            if area>2000:
                max_cnts.append(c) 
        return max_cnts
    
    def cnt_draw(self,c,shape):
        M=cv2.moments(c)
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        cv2.drawContours(self.img,[c],-1,(0,255,0),2)
        cv2.putText(self.img, shape, (cx,cy), 0, 2, (0,255,0), 3)
        
    def cnt_center(self,c):
        M=cv2.moments(c)
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        return [cx,cy]
    
    def face_detect(self, model_name):
        self.path = model_path + model_name + '.xml'
        self.cascade = cv2.CascadeClassifier(self.path)
        self.color_data = 'no_people'
        self.img_new = self.img
        gray = cv2.cvtColor(self.img_new, cv2.COLOR_BGR2GRAY)  # 转换灰色
        faces = self.cascade.detectMultiScale(gray, 2, 5)  # 系数得调。
        if len(faces):  # 大于0则检测到人脸
            self.color_data = '有人'
            for (x, y, w, h) in faces:
                cv2.rectangle(self.img_new, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if x > 0 and y > 0:
                    cv2.rectangle(self.img_new, (x, y), (x + w, y + h), (255, 0, 0), 1)
                    if self.flag_cap == 1 or self.flag_mask == 1:
                        try:
                            drc = cv2.imread(self.pht)
                            src = self.img
                            if self.flag_cap == 1:
                                T, U = int(w), int(h)
                           
                                drc = cv2.resize(drc, (T, U))
                                if y < h:
                                    drc = drc[U - y:U, 0:w]
                                mask = 255 * np.ones(drc.shape, drc.dtype)
                                center = (int((x + w // 2)), y * 10 // 10)
                            if self.flag_mask == 1:
                                T, U = w, h*4//5
                                drc = cv2.resize(drc, (T, U))
                                mask = 255 * np.ones(drc.shape, drc.dtype)
                                center = (int(x + w // 2), int(y + h * 7 // 10))
                            output = cv2.seamlessClone(drc, src, mask, center, cv2.MIXED_CLONE)
                            cv2.imshow('output', output)
                            cv2.waitKey(40)
                        except:
                            pass
        cv2.imshow('face', self.img_new)
        cv2.waitKey(40)
        
    def face_cap(self,path):
        self.pht = d_path + path + '.jpg'
        self.flag_cap = 1
        self.face_detect('face')
        
    def face_mask(self,path):
        self.pht = d_path + path + '.jpg'
        self.flag_mask = 1
        self.face_detect('face')

    def decodeDisplay(self, image):  # 解码部分
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            # 提取条形码的边界框的位置
            # 画出图像中条形码的边界框
            (x, y, w, h) = barcode.rect
            # nts = cv2.findContours(barcode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            # print('x, y, w,h', x, y, w, h)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.circle(image, (int(x + w / 2), int(y + h / 2)), int(h / 2), (255, 0, 0), 5)
        
            if x > 0 and y > 0:
                img_new = image[y:y + h, x:x + w]
                # cv2.imshow('img_new',img_new)
                # cv2.waitKey(0)
            else:
                img_new = image
            # cv2.imshow('img_new',img_new)
            # cv2.waitKey(40)
            # cv2.circle(image, (int(x+w/2), int(y+h/2)), int( h/2), (255, 0, 0), 5)
            # 条形码数据为字节对象，所以如果我们想在输出图像上
            # 画出来，就需要先将它转换成字符串
            barcodeData = barcode.data.decode("utf-8")
            self.er_data = barcodeData

    def erweima_detect(self):
        self.er_data = 'none'
        # 读取当前帧
        # 转为灰度图像
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.decodeDisplay(gray)
        cv2.imshow('erweima', gray)
        cv2.waitKey(1)
        
    def model_(self,model_name='lxy1007.proto'):
        self.model = cv2.dnn.readNetFromONNX(model_path + model_name)  # 如'finally.proto'
        f = model_name.split(".")
        self.item = f[0]
        # print('self.item',self.item)
        self.pro = 0
        self.m_data = 'none'

    def onnx_detect_new(self, img):
        self.model_()
        img = np.asarray(img, dtype=np.float) / 255
        img = img.transpose(2, 0, 1)
        img = img[np.newaxis, :]
        self.model.setInput(img)
        pro = self.model.forward()
        e_x = np.exp(pro.squeeze() - np.max(pro.squeeze()))
        self.pro = e_x / e_x.sum()

    def model_recognize(self):
        frame = cv2.resize(self.img, (224, 224))
        self.onnx_detect_new(frame)
        if np.max(self.pro) > 0.9:
            classNum = np.argmax(self.pro)
            if classNum in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                self.m_data = items_num[classNum]
            elif classNum in [9, 10]:
                self.m_data = items_dir[classNum]
            elif classNum == 11:
                self.m_data = items_label[classNum]
        else:
            self.m_data = 'none'

    def color_detect_init(self,color):
        self.color_data = 'none'  # 保存颜色的检测结果
        if color == 'red':
            self.color_list_lower = [50, 43, 46]  # 这是红色的数值
            self.color_list_upper = [180, 255, 255]
        elif color == 'green':
            self.color_list_lower = [35, 43, 46]
            self.color_list_upper = [77, 255, 255]
        elif color == 'yellow':
            self.color_list_lower = [26, 43, 46]
            self.color_list_upper = [34, 255, 255]
        elif color == 'blue':
            self.color_list_lower = [80, 43, 46]
            self.color_list_upper = [124, 255, 255]
        elif color == 'orange':
            self.color_list_lower = [11, 43, 46]
            self.color_list_upper = [25, 255, 255]
        elif color == 'black':
            self.color_list_lower = [0, 0, 0]
            self.color_list_upper = [180, 255, 46]
        elif color == 'white':
            self.color_list_lower = [0, 0, 221]
            self.color_list_upper = [180, 30, 255]
        elif color == 'gray':
            self.color_list_lower = [0, 0, 46]
            self.color_list_upper = [180, 43, 220]
        elif color == 'purple':
            self.color_list_lower = [125, 43, 46]
            self.color_list_upper = [155, 255, 255]
        elif color == 'qing':
            self.color_list_lower = [78, 43, 46]
            self.color_list_upper = [99, 255, 255]
    
        self.colorLower = np.array(self.color_list_lower)  # 这是红色的数值
        self.colorUpper = np.array(self.color_list_upper)
        self.color = color
        # 初始化追踪点的列表
        self.mybuffer = 16
        self.pts = deque(maxlen=self.mybuffer)
        self.counter = 0
        self.Hmax = self.Smax = self.Vmax = 0
        self.Hmin = self.Smin = self.Vmin = 255

    def set_hsv(self, color):
        image = self.img
        self.HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imshow("imageHSV", self.HSV)
        cv2.imshow('image', image)
        cv2.setMouseCallback("imageHSV", self.getpos)
        cv2.waitKey(0)
        self.color_list_lower = [self.Hmax, self.Smax, self.Vmax]
        self.color_list_upper = [self.Hmin, self.Smin, self.Vmin]
        self.colorLower = np.array(self.color_list_lower)  # 这是红色的数值
        self.colorUpper = np.array(self.color_list_upper)
        self.color = color
        print(self.colorLower)
        print(self.colorUpper)

    def getpos(self, event, x, y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:  # 定义一个鼠标左键按下去的事件
            print(self.HSV[y, x])
            if self.HSV[y, x][0] < self.Hmin:
                self.Hmin = self.HSV[y, x][0]
            if self.HSV[y, x][0] > self.Hmax:
                self.Hmax = self.HSV[y, x][0]
            if self.HSV[y, x][1] < self.Smin:
                self.Smin = self.HSV[y, x][1]
            if self.HSV[y, x][1] > self.Smax:
                self.Smax = self.HSV[y, x][1]
            if self.HSV[y, x][2] < self.Vmin:
                self.Vmin = self.HSV[y, x][2]
            if self.HSV[y, x][2] > self.Vmax:
                self.Vmax = self.HSV[y, x][2]

    def setcolorvalue(self, color, color_list_low, color_list_up):
        self.color_list_lower = color_list_low
        self.color_list_upper = color_list_up
        self.colorLower = np.array(self.color_list_lower)  # 这是红色的数值
        self.colorUpper = np.array(self.color_list_upper)
        self.color = color
        print('设置阈值成功，当前阈值为：', self.color_list_lower, self.color_list_upper)

    def color_detect(self):
        frame = self.img
        self.data = 'none'
        self.frame = frame
        self.img_new = frame
        # 转到HSV空间
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow('hsv',hsv)
        # cv2.waitKey(40)
        # 根据阈值构建掩膜
        mask = cv2.inRange(hsv, self.colorLower, self.colorUpper)
        #         cv2.imshow('mask_original', mask)
        #         cv2.waitKey(40)
        # 腐蚀操作
        mask = cv2.erode(mask, None, iterations=2)
        # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # 初始化识别物体圆形轮廓质心
        center = None
        # 如果存在轮廓
        if len(cnts) > 0:
            # 找到面积最大的轮廓
            c = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)  # 最大面积区域的外接矩形   x,y是左上角的坐标，w,h是矩形的宽和高
            # print('x,y,w,h',x,y,w,h)
            if w > 60 and h > 60:  # 宽和高大于一定数值的才要。
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
                cv2.rectangle(frame_bgr, (x, y), (x + w, y + h), (0, 255, 255), 2)
                # print('x,y,w,h',x,y,w,h)
                if x < 0 or y < 0:
                    # self.img_new=frame_bgr
                    self.img_new = frame
                else:
                    # self.img_new=frame_bgr[y:y+h,x:x+w]
                    self.img_new = frame[y:y + h, x:x + w]
                # cv2.imshow('img_new', self.img_new)
                # cv2.waitKey(3)
    
            # 确定面积最大的轮廓的外接圆
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            self.x = x
            self.y = y
            self.radius = radius
            # 计算轮廓的矩
            M = cv2.moments(c)
            # 计算质心
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # 只有当半径大于100mm时，才执行画图
            if radius > 5:
                # img_circle=cv2.circle(self.frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # cv2.circle(self.frame, center, 5, (0, 0, 255), -1)

                # 把质心添加到pts中，并且是添加到列表左侧
                self.pts.appendleft(center)
                # cv2.imshow('color', self.frame)
                # cv2.waitKey(1)
                self.color_data = self.color

        else:  # 如果图像中没有检测到识别物体，则清空pts，图像上不显示轨迹。
            self.pts.clear()
            # cv2.imshow('color', self.frame)
            # cv2.waitKey(1)
            self.color_data = 'other_color'


# def f1():#寻迹简化案例
#     a=Camera(0)
#     while True:
#         start_time=time.time()
#         img=Img(a.read_camera())
#         img.name_windows("1")
#         if img.offset2():
#             if img.dotted_line2():
#                 print("这是虚线")
#             else:
#                 d=img.offset_calculate2()
#                 print("线路偏移量:"+str(d))
#                 e=img.line_angle2()
#                 print("线路角度:"+str(e))
#         else:
#             print("未识别到线路")
#         img.show_image("1")
#         end_time=time.time()
#         times_re=end_time-start_time
#         print("time:",times_re)
#     a.close_camera()
# def f2():
#     a=Camera(0)
#     while True:
#         img=Img(a.read_camera())
#         img1=Img(a.read_camera())
#         img.name_windows("1")
#         img1.name_windows("2")
#         img.BGR2GRAY()
#         img.GRAY2BIN()
#         cnts=img.bin_detect()
#         for c in cnts:
#             if img.detect(c,"圆形"):
#                 img1.cnt_draw(c,"1")
#         img.show_image("1")
#         img1.show_image("2")
#     a.close_camera()
# def f3():
#     img=Img(pic_read("1.png"))
#     img1=Img(pic_read("1.png"))
#     img.BGR2GRAY()
#     img.GRAY2BIN()
#     img1.name_windows("1")
#     cnts=img.bin_detect()
#     for c in cnts:
#         if img.detect(c,"圆形"):
#             img1.cnt_draw(c,"circle")
#     img1.show_image("1")
# if __name__=='__main__':
#     f2()

# def main():
#     a=Camera(0)
#     while True:
#         img = Img(a.read_camera())
#         img.model_recognize()
#         img.color_detect_init('red')
#         img.color_detect()
#         new_img = Img(img.img_new)
#         new_img.name_windows('22')
#         new_img.show_image('22')
#         print(img.m_data)
#         print(img.color_data)
# main()