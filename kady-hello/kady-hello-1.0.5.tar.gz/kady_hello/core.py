import json

class HSResult:
    # 0 表示 正常状态，-1 表示非正常状态
    status = None
    #消息内容
    message = ""
    #对象体
    data=None

    @staticmethod
    def saySuccess(message):
        result = HSResult()
        result.status = 0
        result.message = message
        return result

    @staticmethod
    def sayFail(message):
        result = HSResult()
        result.status = -1
        result.message = message
        return result

    #转换成json字符串
    def toJSON(self):
        return json.dumps(self,ensure_ascii=False,default=lambda o: o.__dict__, sort_keys=True, indent=4)

    #携带数据
    def withData(self,data):
        self.data = data
        return self


def line(number):
    if number == None:
        number = 0
    print("\n\n<%s> ----------------------"
          "---------------------------"
          "---------------------------"
          "---------------------------"
          "------------"%(number))
