import datetime
import json
import numpy as np
import pandas as pd
from typing import List, Optional
import webbrowser

from pyrasgo.api.connection import Connection
from pyrasgo.api.error import APIError
from pyrasgo.api.create import Create
from pyrasgo.schemas.feature import featureImportanceStats 
from pyrasgo.utils.monitoring import track_usage

class Evaluate(Connection):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create = Create(api_key=self._api_key)

    @track_usage
    def calculate_feature_importance(self, df: pd.DataFrame, 
                                    target_column: str, 
                                    exclude_columns: List[str] = None,
                                    return_cli_only: bool = False
                                    ) -> dict:
        """
        Calculates importance of a target feature using Shapley values. Opens a page in the 
        Rasgo WebApp with feature importance graph OR return raw json of feature importance.

        params:
        df: pandas DataFrame
        target_columns: string: column name of target feature
        exclude_columns: list of strings: column names of date features to be filered out from calculation
        return_cli_only: instructs function to not open Rasgo WebApp and return json in the CLI only

        """
        # Check if we can run this
        try:
            import shap
            import catboost
            from sklearn.metrics import mean_squared_error
            from sklearn.metrics import r2_score
        except ModuleNotFoundError:
            raise APIError('These packages will need to be installed to run this function: catboost, shap, sklearn')

        if target_column not in df.columns:
            raise APIError(f'Column {target_column} does not exist in DataFrame')

        # Prep DataFrame
        # NOTE: Nulls cause a problem with the importance calc:
        df = df.dropna()
        # NOTE: Dates cause a problem with the importance cals:
        df = df.select_dtypes(exclude=['datetime'])
        if exclude_columns:
            for col in exclude_columns:
                df = df.drop(col, 1)

        # Create x and y df's based off target column
        df_x = df.loc[:, df.columns != target_column]
        df_y = df.loc[:, df.columns == target_column]
        
        # Get categorical feature indices to pass to catboost
        cat_features = np.where(df_x.dtypes != np.number)[0]

        # Create the catboost dataset
        try:
            dataset = catboost.Pool(data=df_x, label=df_y, cat_features=cat_features)
        except TypeError as e:
            raise APIError(f"Catboost error: {e}: "
                           f"One or more of the fields in your dataframe is a date that cannot be automatically filtered out. "
                           f"You can use the exclude_fields=[''] parameter to exclude these manually and re-run this fuction.")
        model = catboost.CatBoostRegressor(iterations=300, random_seed=123)
        model.fit(dataset, verbose=False, plot=False)
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(dataset)
        df_shap = pd.DataFrame(shap_values, columns=df_x.columns)

        # Start building output json
        c_data = {}
        c_data["targetFeature"] = target_column

        # Histogram binning of shapley values
        c_data['featureShapleyDistributions'] = {}
        for column in df_shap:
            try:
                H, xedges, yedges = np.histogram2d(x=df[column], y=df_shap[column], bins=10)
                df_hist = pd.DataFrame(zip(H.tolist(), xedges, yedges), columns=['Histogram','feature_edges','shap_edges'])
                fhist = df_hist.to_dict(orient="list")
                c_data['featureShapleyDistributions'][column] = fhist
            except:
                count, division = np.histogram(df_shap[column], bins=25, density=False)
                df_hist = pd.DataFrame(zip(count, division), columns=['Count','Bound'])
                fhist = df_hist.to_dict(orient="records")
                c_data['featureShapleyDistributions'][column] = fhist
        # Mean absolute value by feature
        c_data['featureImportance'] = df_shap.abs().mean().to_dict()
        
        # TODO: Split train and test when supported
        
        # Model performance
        c_data['modelPerformance'] = {}
        pred = model.predict(df_x)
        rmse = (np.sqrt(mean_squared_error(df_y, pred)))
        r2 = r2_score(df_y, pred)
        c_data['modelPerformance']['RMSE'] = rmse
        c_data['modelPerformance']['R2'] = r2
        
        if return_cli_only:
            return {
                    "targetfeature": target_column,
                    "featureImportance": c_data['featureImportance']
                }
        else:
            json_payload = featureImportanceStats(
                targetFeature= target_column,
                featureShapleyDistributions= c_data['featureShapleyDistributions'],
                featureImportance= c_data['featureImportance'],
                modelPerformance= c_data['modelPerformance']
            )
            
            # create a unique id
            uid = self._make_dataframe_id()
            
            # save json to Api
            self.create.column_importance_stats(id = uid, payload = json_payload)
            
            # open the profile in a web page
            url = f'https://{self._environment.app_path}/dataframes/{uid}/importance'
            webbrowser.open(url)
            return 'Profile available at: ' + url

    @track_usage
    def find_duplicate_rows(self, df: pd.DataFrame, 
                            columns: List[str] = None) -> pd.DataFrame:
        """ 
        Returns a DataFrame of rows that are duplicated in your original DataFrame 
        
        df: pandas DataFrame
        columns: (Optional) List of column names to check for duplicates in
        """
        df_out = df.copy(deep=True)
        if columns:
            df_out = df.iloc[:0].copy()
            for column in columns:
                df_out = df_out.append(df[df.duplicated([column])])
        else:
            df_out = df[df.duplicated()]
        return df_out

    @track_usage
    def find_missing_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """ 
        Print all columns in a Dataframe with null values
        and return rows with null values
        
        Response:   Columns with null values:
                    -------------------------
                    column, count of rows
                    -------------------------
                    List[index of rows with null values]
        
        df: pandas DataFrame
        """
        column_with_nan = df.columns[df.isnull().any()]
        template="%-20s %-6s"
        print(template % ("Column", "Count of Nulls"))
        print("-"*35)
        for column in column_with_nan:
            print(template % (column, df[column].isnull().sum()))
        print("-"*35)
        return df[df.isnull().any(axis=1)]

    @track_usage
    def find_type_mismatches(self, df: pd.DataFrame, 
                             column: str, 
                             data_type: str) -> pd.DataFrame:
        """ 
        Return a copy of your DataFrame with a column cast to another datatype
        
        df: pandas DataFrame
        column: The column name in the DataFrame to cast
        data_type: the data type to cast to Accepted Values: ['datetime', 'numeric']
        """
        new_df = pd.DataFrame()
        if data_type == 'datetime':
            new_df[column] = pd.to_datetime(df[column], errors='coerce', infer_datetime_format=True)
        elif data_type == 'numeric':
            new_df[column] = pd.to_numeric(df[column], errors='coerce')
        else:
            return "Supported data_type values are: 'datetime' or 'numeric'"
        total = df[column].count()
        cant_convert = new_df[column].isnull().sum()
        print(f"{(total - cant_convert) / total}%: {cant_convert} rows of {total} rows cannot convert.")
        new_df.rename(columns = {column:f'{column}CastTo{data_type.title()}'}, inplace = True)
        return new_df

    @track_usage
    def scan_for_timeseries_gaps(self, df: pd.DataFrame, 
                                 column: str):
        # Return rows before and after timeseries gaps 
        return NotImplementedError('Coming Soon')

    def _make_dataframe_id(self) -> int:
        org_id = self._profile.get('organizationId')
        user_id = self._profile.get('id')
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return str(org_id)+str(user_id)+timestamp