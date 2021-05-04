from sklearn.feature_extraction import DictVectorizer
from kolibri.core.component import Component
from kdmt.dict import update



class DataFieldSelector(Component):
    """For data grouped by feature, select subset of data at a provided key.

    The data is expected to be stored in a 2D data structure, where the first
    index is over features and the second is over samples.  i.e.

    >> len(data[key]) == n_samples

    Please note that this is the opposite convention to scikit-learn feature
    matrixes (where the first index corresponds to sample).

    ItemSelector only requires that the collection implement getitem
    (data[key]).  Examples include: a dict of lists, 2D numpy array, Pandas
    DataFrame, numpy record array, etc.

    >> data = {'a': [1, 5, 2, 5, 2, 8],
               'b': [9, 4, 1, 4, 1, 3]}
    >> ds = DataFieldSelector(key='a')
    >> data['a'] == ds.transform(data)


    Parameters
    ----------
    key : hashable, required
        The key corresponding to the desired value in a mappable.
    """

    name = "data_field_selector"

    hyperparameters= {
        "fixed": {
            'data-type': 'json', #dataframe, array
            'field-name': None
        },

        "tunable": {
        }
    }


    def __init__(self, parameters, field_name=None):
        self.hyperparameters=update(self.hyperparameters, DataFieldSelector.hyperparameters)
        super().__init__(parameters)
        if field_name is None:
            self.key = self.get_prameter('field-name')
        else:
            self.key=field_name
            self.hyperparameters['fixed']['field-name']=field_name

        if self.key is None:
            raise ValueError('key cannot be None in DataFieldSelector')
        self.data_transformer=None
        if self.get_prameter('data-type')=='json':
            self.data_transformer=DictVectorizer(sparse=False)
        elif self.get_prameter('data-type')=='array':
            if not isinstance(self.key, int):
                raise ValueError("When 'data-type' value is 'array', 'key' should be an interger")

    def fit(self, X, y=None):
        if self.data_transformer is not None:
            self.data_transformer.fit(X, y)
        return self

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)


    def transform(self, data_dict):
        key_id=self.key
        if self.data_transformer is not None:
            data_dict = self.data_transformer.transform(data_dict)
            if self.key in self.data_transformer.feature_names_:
                key_id=self.data_transformer.feature_names_.index(self.key)
            else:
                raise ValueError('key {} not in data dictionnary'.format(self.key))

        if self.get_prameter('data-type') in ['json', 'array']:
            return data_dict[:, key_id]

        return data_dict[self.key]
    def get_info(self):
        return "data_field_selector"


from kolibri.registry import ModulesRegistry
ModulesRegistry.add_module(DataFieldSelector.name, DataFieldSelector)






