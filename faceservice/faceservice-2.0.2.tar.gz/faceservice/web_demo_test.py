import requests
import cv2

from faceservice.lib.web.http import app


from config import config as cfg



url='http://192.168.97.134:5000/peppa_pig_face_engine/excuter'


#pic_path="./figure/test1.jpg"
pic_path="/Users/jfu/workspace/faceservice/figure/test1.jpg"

res = {"image":open(pic_path,'rb')}

img = cv2.imread(pic_path)
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)



res = requests.post(url,data=img_encoded.tostring())

print(res.content)