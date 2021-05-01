import pandas as pd
import numpy as np
from datetime import datetime
import time
from .DataModel import DataModel

class EzCohort(DataModel):
    def __init__(self):
        super().__init__()
        self.prep_data = 'EzCohort'
        self.basketDate = 'basketDate'
        self.orderDate = 'orderDate'
        self.cohortGrp = 'cohortGrp'
        self.cohortIdx = 'cohortIdx'

    def get_month(self, x):
        """
        return: datetime object
        """
        return datetime(x.year, x.month, 1)

    def get_date_int(self, column: str):
        """
        column <- column name containing invoice or order date
        return: tuple
        """
        series = pd.to_datetime(self.prep_data[column])
        year = series.dt.year
        month = series.dt.month
        day = series.dt.day
        return year, month, day

    def get_cohort_index(self):
        basket_y, basket_m, basket_d = self.get_date_int(self.basketDate)
        cohort_y, cohort_m, cohort_d = self.get_date_int(self.cohortGrp)
        cohort_idx = (12*(basket_y - cohort_y) + (basket_m - cohort_m)) + 1
        self.prep_data[self.cohortIdx] = cohort_idx

    def prep_cohort(self, data, customerId, orderId, orderDate, salesPrice, date='full', method=None):
        self.prep_data = self.prep(data, customerId, orderId, orderDate, salesPrice)
        self.prep_data[self.basketDate] = self.prep_data['orderDate'].apply(self.get_month)
        self.prep_data = self.prep_data.groupby(['customerId', self.basketDate]).agg(
            frequency=pd.NamedAgg(column='orderId', aggfunc='nunique'),
            salesPrice=pd.NamedAgg(column='salesPrice', aggfunc='sum')
        ).reset_index()
        self.prep_data[self.cohortGrp] = self.prep_data.groupby('customerId')[self.basketDate].transform('min')
        self.get_cohort_index()
        self.prep_data['customerId'] = self.prep_data['customerId'].astype('object')
        return self.prep_data

    def get_cohort_count(self):
        self.prep_data = pd.pivot_table(self.prep_data, index='cohortGrp',columns='cohortIdx',values='customerId',aggfunc='nunique')
        return self.prep_data

    def get_cohort_retention(self):
        self.prep_data = self.prep_data.divide(self.prep_data.iloc[:,0], axis=0)
        return self.prep_data

    def get_cohort_sales(self):
        res = pd.pivot_table(self.prep_data, index='cohortGrp',columns='cohortIdx',values='salesPrice',aggfunc='sum')
        return res

    def get_cohort_frequency(self):
        res = pd.pivot_table(self.prep_data, index='cohortGrp',columns='cohortIdx',values='frequency',aggfunc='sum')
        return res

    def get_cohort_mean(self):
        total = self.get_cohort_sales()
        freq = self.get_cohort_frequency()
        self.prep_data = total.divide(freq)
        return self.prep_data

    def get_melt(self):
        self.prep_data = self.prep_data.reset_index()
        self.prep_data = pd.melt(self.prep_data, id_vars=self.cohortGrp)
        return self.prep_data

    def fit(self, data, customerId, orderId, orderDate, salesPrice, date='full', method='count', melt=False):
        """
        method = retention_rate, qty, sales, avg
        """
        self.prep_cohort(data, customerId, orderId, orderDate, salesPrice, date='full', method=None)
        if method=='count':
            self.prep_data = self.get_cohort_count()
        elif method=='retention':
            self.prep_data = self.get_cohort_count()
            self.prep_data = self.get_cohort_retention()
        elif method=='sales':
            self.prep_data = self.get_cohort_sales()
        elif method=='frequency':
            self.prep_data = self.get_cohort_frequency()
        elif method=='mean':
            self.get_cohort_mean()
        else:
            self.prep_data

        if melt==True:
            self.get_melt()
        
        return self.prep_data.round(2)