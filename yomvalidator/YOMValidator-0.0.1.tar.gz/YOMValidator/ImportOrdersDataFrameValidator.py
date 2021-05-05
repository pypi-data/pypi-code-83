import pandas as pd
import pandera as pa


class ImportOrdersDataFrameValidator():
    def __init__(self):
        self.schema = pa.DataFrameSchema({
            # Required data
            'orderId': pa.Column(pa.String, nullable=False),
            'productId': pa.Column(pa.String, nullable=False),
            'userId': pa.Column(pa.String, nullable=False),
            'date': pa.Column(pa.DateTime, nullable=False),
            'documentType': pa.Column(pa.String, nullable=False),
            'documentCode': pa.Column(pa.String, nullable=False),
            'quantity': pa.Column(pa.Float, nullable=False),
            'pricePerUnit': pa.Column(pa.Float, nullable=False),
            'tax': pa.Column(pa.Float, nullable=False),
            'discountPerUnit': pa.Column(pa.Float, nullable=False),
            'currency': pa.Column(pa.String, nullable=False),
            'origin': pa.Column(pa.String, nullable=False),
            # Recommended data
            'sellerId': pa.Column(pa.String, nullable=False, required=False),
            'sellerRouteId': pa.Column(pa.String, nullable=False, required=False),
            'deliveryDate': pa.Column(pa.DateTime, nullable=False, required=False),
            'referenceCode': pa.Column(pa.String, nullable=False, required=False),
            'deleted':  pa.Column(pa.String, nullable=False, required=False, checks=pa.Check.isin(['true', 'false'])),
        })


    def validate(self, dataframe):
        return self.schema.validate(dataframe)