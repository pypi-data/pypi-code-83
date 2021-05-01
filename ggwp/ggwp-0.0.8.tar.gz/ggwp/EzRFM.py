import pandas as pd
import numpy as np
from datetime import datetime
import time
from .DataModel import DataModel

class EzRFM(DataModel):
    def __init__(self):
        super().__init__()
        self.prep_data = 'EzRMF'

    def prep_rfmt(self, data):
        target = data[self.orderDate].max() + np.timedelta64(1,'D')
        data = data.groupby(self.customerId).agg(
            totalRecency=pd.NamedAgg(column=self.orderDate, aggfunc=lambda x: (target-x.max()).days),
            totalFrequency=pd.NamedAgg(column=self.orderId, aggfunc='nunique'),
            totalMonetary=pd.NamedAgg(column=self.salesPrice, aggfunc='sum'),
            totalTenure=pd.NamedAgg(column=self.orderDate, aggfunc=lambda x: (target-x.min()).days),
            totalSizeMin=pd.NamedAgg(column=self.salesPrice, aggfunc='min'),
            totalSizeQ1=pd.NamedAgg(column=self.salesPrice, aggfunc=lambda x: x.quantile(.25)),
            totalSizeMean=pd.NamedAgg(column=self.salesPrice, aggfunc='mean'),
            totalSizeMedian=pd.NamedAgg(column=self.salesPrice, aggfunc='median'),
            totalSizeQ3=pd.NamedAgg(column=self.salesPrice, aggfunc=lambda x: x.quantile(.75)),
            totalSizeMax=pd.NamedAgg(column=self.salesPrice, aggfunc='max'),
            totalSizeStd=pd.NamedAgg(column=self.salesPrice, aggfunc='std'),
            totalSizeRange=pd.NamedAgg(column=self.salesPrice, aggfunc=lambda x: x.max()-x.min()),
            totalSizeSkew=pd.NamedAgg(column=self.salesPrice, aggfunc='skew'),)
        
        return data.reset_index().fillna(0).round(2)

    def prep_rfmt_date(self, data, column, method):
        data = data.groupby([self.customerId,column]).agg({
            self.orderId:'nunique',
            self.salesPrice:'sum'
        }).reset_index()

        data = data.groupby(self.customerId).agg({
            column:'nunique',
            self.orderId:['mean','median','std'],
            self.salesPrice:['min', self.get_q1, 'mean', 'median', 
                             self.get_q3, 'max','std', self.get_range,'skew']
        }).reset_index()

        names = ['FrequencySum','FrequencyMean','FrequencyMedian','FrequencyStd',
                 'MonetaryMin','MonetaryQ1','MonetaryMean','MonetaryMedian',
                 'MonetaryQ3','MonetaryMax','MonetaryStd','MonetaryRange','MonetarySkew']
        data.columns = [self.customerId] + [method +  name for name in names]

        return data

    def fit(self, data, customerId, orderId, orderDate, salesPrice, method=None):
        
        start = time.time()

        init_df = self.prep(data, customerId, orderId, orderDate, salesPrice)
        rfmt_df = self.prep_rfmt(init_df)
        # total_visit = rfmt_df['totalFrequency']

        method_list = ['year','quarter','month','week'] 

        if method == None:
            rfmt_df = rfmt_df
        else:
            if method == 'year':
                columns = ['year']
            elif method == 'quarter':
                columns = ['yearQuarter']
            elif method == 'month':
                columns = ['yearMonth']
            elif method == 'week':
                columns = ['yearWeek']
            elif method == 'full':
                columns = ['year','yearQuarter','yearMonth','yearWeek']

            for enum, column in enumerate(columns):        
                rfmt_date = self.prep_rfmt_date(init_df, column, method_list[enum])
                rfmt_df = pd.concat([rfmt_df, rfmt_date.drop('customerId',axis=1)],axis=1)

        print('successfully preped EzRFM {:.4f} ms'.format(time.time()-start))

        return rfmt_df