import pandas as pd
import pandera as pa


class ImportProductsDataFrameValidator():
    def __init__(self):
        self.schema = pa.DataFrameSchema({
            # Required data
            'productId': pa.Column(pa.String, nullable=False),
            'sku': pa.Column(pa.String, nullable=False),
            'name': pa.Column(pa.String, nullable=False),
            'blocked': pa.Column(pa.Boolean, nullable=False),
            'amountPerPackage': pa.Column(pa.Float, nullable=False),
            'packageUnit': pa.Column(pa.String, nullable=False),
            'boxUnit': pa.Column(pa.String, nullable=False),
            'amountPerBox': pa.Column(pa.Float, nullable=False),
            'salesUnit': pa.Column(pa.String, nullable=False),
            # Recommended data
            'description': pa.Column(pa.String, nullable=False, required=False),
            'category': pa.Column(pa.String, nullable=False, required=False),
            'subcategory': pa.Column(pa.String, nullable=False, required=False),
            'brand': pa.Column(pa.String, nullable=False, required=False),
            'price': pa.Column(pa.Float, nullable=False, required=False),
            'suggestionUnit': pa.Column(pa.String, nullable=False, required=False),
            'categoricalLevel1': pa.Column(pa.String, nullable=False, required=False),
            'categoricalLevel2': pa.Column(pa.String, nullable=False, required=False),
            'categoricalLevel3': pa.Column(pa.String, nullable=False, required=False),
            'deleted':  pa.Column(pa.String, nullable=False, required=False, checks=pa.Check.isin(['true', 'false'])),
        })


    def validate(self, dataframe):
        return self.schema.validate(dataframe)