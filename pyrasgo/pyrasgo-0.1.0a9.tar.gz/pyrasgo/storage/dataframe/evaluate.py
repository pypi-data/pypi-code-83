import datetime
import numpy as np
import pandas as pd
from typing import List
import webbrowser

from pyrasgo.api.connection import Connection
from pyrasgo.api.error import APIError
from pyrasgo.api.create import Create
from pyrasgo.schemas.feature import featureImportanceStats, ColumnProfiles
from pyrasgo.utils.monitoring import track_usage

class Evaluate(Connection):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create = Create(api_key=self._api_key)

    @track_usage
    def calculate_feature_importance(self, df: pd.DataFrame, 
                                    target_column: str, 
                                    exclude_columns: List[str] = None,
                                    return_cli_only: bool = False,
                                    rasgo_df_id: int = None
                                    ) -> dict:
        """
        Calculates importance of a target feature using Shapley values. Opens a page in the 
        Rasgo WebApp with feature importance graph OR return raw json of feature importance.

        params:
        df: pandas DataFrame
        target_columns: string: column name of target feature
        exclude_columns: list of strings: column names of date features to be filered out from calculation
        return_cli_only: instructs function to not open Rasgo WebApp and return json in the CLI only
        rasgo_df_id: optional int, allows user to manually associate this dataframe with a previous run of feature importance
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

        # assign a unique id to the DF before we alter it
        if rasgo_df_id:
            self._tag_dataframe(df, {"RasgoID": rasgo_df_id})
        else:
            rasgo_df_id = self._make_dataframe_id(df)

        # Copy df so we can alter it without impacting source data
        fi_df = df.copy(deep=True)
        
        # Prep DataFrame
        # NOTE: Nulls cause a problem with the importance calc:
        fi_df = fi_df.dropna()
        # NOTE: Dates cause a problem with the importance cals:
        fi_df = fi_df.select_dtypes(exclude=['datetime'])
        if exclude_columns:
            for col in exclude_columns:
                fi_df = fi_df.drop(col, 1)

        # Create x and y df's based off target column
        df_x = fi_df.loc[:, fi_df.columns != target_column]
        df_y = fi_df.loc[:, fi_df.columns == target_column]
        
        # Get categorical feature indices to pass to catboost
        cat_features = np.where(df_x.dtypes != np.number)[0]

        # Create the catboost dataset
        try:
            dataset = catboost.Pool(data=df_x, label=df_y, cat_features=cat_features)
        except TypeError as e:
            raise APIError(f"Catboost error: {e}: "
                           f"One or more of the fields in your dataframe is a date that cannot be automatically filtered out. "
                           f"You can use the exclude_columns=[''] parameter to exclude these manually and re-run this fuction.")
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
                H, xedges, yedges = np.histogram2d(x=fi_df[column], y=df_shap[column], bins=10)
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
            
            # save json to Api
            self.create.column_importance_stats(id = rasgo_df_id, payload = json_payload)
            
            # open the profile in a web page
            url = f'https://{self._environment.app_path}/dataframes/{rasgo_df_id}/importance'
            webbrowser.open(url)
            return 'Profile available at: ' + url

    @track_usage
    def generate_profile(self, df: pd.DataFrame, 
                         exclude_columns: List[str] = None,
                         return_cli_only: bool = False,
                         rasgo_df_id: int = None) -> dict:
        """Profile a DataFrame locally, and push metadata to rasgo to display.

        df: pandas DataFrame
        return_cli_only: instructs function to not open Rasgo WebApp and return json in the CLI only
        rasgo_df_id: optional int, allows user to manually associate this dataframe with a previous run of feature importance
        """
        # assign a unique id to the DF before we alter it
        if rasgo_df_id:
            self._tag_dataframe(df, {"RasgoID": rasgo_df_id})
        else:
            rasgo_df_id = self._make_dataframe_id(df)

        # Copy df so we can alter it without impacting source data
        p_df = df.copy(deep=True)
        # Remove columns before profiling
        if exclude_columns:
            for col in exclude_columns:
                p_df = p_df.drop(col, 1)

        # Create an object to hold intermediate data calculated via pandas
        profile_data = {}
        for col_label in p_df:
            profile_data[col_label] = {}

        # label is the name of the attribute in the api request/response
        # mean is the name of the pandas function that calculates it
        # last item is any kwargs required for the function
        labels_and_functions = [
            ('recCt', 'count', {'axis': 0}),
            ('distinctCt', 'nunique', None),
            ('meanVal', 'mean', {'axis': 0, 'numeric_only': True}),
            ('medianVal', 'median', {'axis': 0, 'numeric_only': True}),
            ('maxVal', 'max', {'axis': 0, 'numeric_only': True}),
            ('minVal', 'min', {'axis': 0, 'numeric_only': True}),
            ('sumVal', 'sum', {'axis': 0, 'numeric_only': True}),
            ('stdDevVal', 'std', {'axis': 0, 'numeric_only': True})
        ]
        for label, func_name, extra_args in labels_and_functions:
            results = self._evaluate_df(p_df, func_name, extra_args)
            for col_label in p_df:
                try:
                    # store under key name for column, if the value exists
                    profile_data[col_label][label] = results[col_label]
                except KeyError:
                    pass

        response = {
            'columnProfiles': []
        }
        for col_label in profile_data:
            column_stats = {
                'columnName': col_label,
                'dataType': p_df[col_label].dtype.name,
                'featureStats': profile_data[col_label]
            }
            response['columnProfiles'].append(column_stats)

        if return_cli_only:
            return response
        else:
            json_payload = ColumnProfiles(**response)

            # save json to Api
            self.create.dataframe_profile(id=rasgo_df_id, payload=json_payload)

            # open the feature profiles in a web page
            url = f'https://{self._environment.app_path}/dataframes/{rasgo_df_id}/features'
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

    def _make_dataframe_id(self, df: pd.DataFrame) -> int:
        """Calculates a deterministic (and hopefully unique) ID for a dataframe and tags it"""
        from pyrasgo.utils.naming import hash_list
        # If df is already marked with an ID, keep it
        if df.attrs.get("RasgoID"):
            return df.attrs["RasgoID"]
        # Else calcualte a new ID
        org_id = self._profile.get('organizationId')
        user_id = self._profile.get('id')
        column_hash = hash_list(df.columns)
        # Note: Dataframe are likely to have the same columns often, adding date will help us de-dup
        # but won't allow users to tie back dataframes across Rasgo sessions 
        day = datetime.datetime.now().strftime('%Y%m%d')
        unique_id = str(org_id)+str(user_id)+day+str(column_hash)
        # Tag the df with the ID so we can keep track of it after columns are dropped
        self._tag_dataframe(df, {"RasgoID": unique_id})
        return unique_id

    def _tag_dataframe(self, df: pd.DataFrame, attribute: dict):
        """Tags a dataframe with an attribute"""
        write_back_attrs = df.attrs or {}
        write_back_attrs.update(attribute)
        df.attrs = write_back_attrs

    @classmethod
    def _evaluate_df(cls, df: pd.DataFrame, func_name: str, extra_args: dict):
        extra_args = extra_args or {}
        # Get the correct DataFrame function by name
        results = getattr(df, func_name)(**extra_args)
        return results
