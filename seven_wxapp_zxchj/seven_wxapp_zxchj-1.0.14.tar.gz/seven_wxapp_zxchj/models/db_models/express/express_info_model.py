
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class ExpressInfoModel(BaseModel):
    def __init__(self, db_connect_key='db_wxapp', sub_table=None, db_transaction=None, context=None):
        super(ExpressInfoModel, self).__init__(ExpressInfo, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class ExpressInfo:

    def __init__(self):
        super(ExpressInfo, self).__init__()
        self.id = 0  # 
        self.express_name = ""  # 物流名称
        self.express_no = ""  # 物流编码
        self.custom_name = ""  # 自定义物流名称
        self.custom_no = ""  # 自定义物流编码
        self.create_date = "1900-01-01 00:00:00"  # 创建时间

    @classmethod
    def get_field_list(self):
        return ['id', 'express_name', 'express_no', 'custom_name', 'custom_no', 'create_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "express_info_tb"
    