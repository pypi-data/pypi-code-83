import pandas as pd
import pandera as pa

class ImportClientDataFrameValidator():
    def __init__(self):
        self.schema = pa.DataFrameSchema({
            # Required data
            'userId': pa.Column(pa.String, nullable=False),
            'name': pa.Column(pa.String, nullable=False),
            'sellerId': pa.Column(pa.String, nullable=False),
            'supervisorId': pa.Column(pa.String, nullable=False),
            'fullAddress': pa.Column(pa.String, nullable=False),
            'commune': pa.Column(pa.String, nullable=False),
            'country': pa.Column(pa.String, nullable=False),
            'city': pa.Column(pa.String, nullable=False),
            # Recommended data
            'active': pa.Column(pa.Boolean, nullable=False, required=False),
            'channel': pa.Column(pa.String, nullable=False, required=False),
            'subChannel': pa.Column(pa.String, nullable=False, required=False),
            'class': pa.Column(pa.String, nullable=False, required=False),
            'globalUserId': pa.Column(pa.String, nullable=False, required=False),
            'region': pa.Column(pa.String, nullable=False, required=False),
            'visitPlan': pa.Column(pa.String, nullable=False, required=False),
            'keyUser': pa.Column(pa.Boolean, nullable=False, required=False),
            'administrativeLevel1': pa.Column(pa.String, nullable=False, required=False),
            'administrativeLevel2': pa.Column(pa.String, nullable=False, required=False),
            'administrativeLevel3': pa.Column(pa.String, nullable=False, required=False),
            'logisticalLevel1': pa.Column(pa.String, nullable=False, required=False),
            'logisticalLevel2': pa.Column(pa.String, nullable=False, required=False),
            'logisticalLevel3': pa.Column(pa.String, nullable=False, required=False),
            'deleted': pa.Column(pa.String, nullable=False, required=False, checks=pa.Check.isin(['true', 'false'])),
        })


    def validate(self, dataframe):
        return self.schema.validate(dataframe)