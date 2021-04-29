from testindatadev.TDA import TDA

T_key = "0fbe149adf07e5f4afa01a7a4e787fde"
ip = "10.32.144.73"

tda = TDA(T_key, True)
tda.SetDataset("ds_m0jgn3k7qyfwl_s984u9", ip)

print(tda.UploadFileToDataset("/Users/hejinlong/Desktop/test_pic/11.jpg"))

# print(tda.UploadFilesToDataset("/Users/hejinlong/Desktop/test_pic/kitti/kitti1/", ext=".png"))