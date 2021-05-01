import pandas as pd
import numpy as np
from datetime import datetime
import time
from .DataModel import DataModel
from .EzCohort import EzCohort

class EzCustomerMovement(EzCohort):
    def __init__(self):
        super().__init__()
        self.prep_data = 'EzCustomerMovement'

    def status_code(self, x):
        if x == 0:
            return 'new'
        elif x == 1:
            return 'repeat'
        elif x > 1:
            return 'reactivate'

    def get_status(self):
        self.prep_data['shift'] = self.prep_data.groupby('customerId')[self.cohortIdx].shift(1).fillna(1).astype('int')
        self.prep_data['statusId'] = self.prep_data[self.cohortIdx] - self.prep_data['shift']
        self.prep_data['status'] = self.prep_data['statusId'].apply(self.status_code)

    def get_churn(self):
        self.prep_data = pd.pivot_table(self.prep_data, 
                                        index=self.basketDate,columns='status',values='customerId',
                                        aggfunc='count',fill_value=0)
        self.prep_data['not_new'] = self.prep_data['reactivate'] + self.prep_data['repeat']
        self.prep_data['cumsum'] = self.prep_data['new'].cumsum().fillna(0)
        self.prep_data['churn'] = self.prep_data['new'] + self.prep_data['not_new']-self.prep_data['cumsum']
        self.prep_data = self.prep_data.reset_index()    

    def prep_customer_movement(self, data, customerId, orderId, orderDate, salesPrice, date, method):
        self.prep_data = self.prep_cohort(data, customerId=customerId, orderId=orderId, orderDate=orderDate, salesPrice=salesPrice)
        self.get_status()
        self.get_churn()
        return self.prep_data

    def get_melt(self):
        self.prep_data = pd.melt(self.prep_data, id_vars=self.basketDate)
        return self.prep_data

    def fit(self, data, customerId, orderId, orderDate, salesPrice, date='full',method=None, melt=True):
        """
        method = normal, melt
        """
        start = time.time()
        columns = [self.basketDate,'new','reactivate','repeat','churn']
        self.prep_data = self.prep_customer_movement(data, customerId, orderId, orderDate, salesPrice, date, method)[columns]
        
        if melt==True:
            self.prep_data = self.get_melt()

        print('successfully preped EzCustomerMovement{:.4f} ms'.format(time.time()-start))
        return self.prep_data