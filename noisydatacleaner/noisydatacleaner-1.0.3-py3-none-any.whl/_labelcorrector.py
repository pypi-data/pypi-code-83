from collections import Counter
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import warnings
warnings.filterwarnings(action='ignore')

class LabelCorrector():
    def __init__(self):
        self.pred_threshold = 0.8
        self.split_ratio = 0.2
        self.pred_iteration = 1000
        self.epoch = 10
        self.classification_models = {
            'Random Forest': RandomForestClassifier(n_estimators=128),
            'Extra Trees': ExtraTreesClassifier(n_estimators=128),
            'Linear Discriminant': LinearDiscriminantAnalysis(),
            'Logistic Regression': LogisticRegression(max_iter=128),
            'Neural Network': MLPClassifier(hidden_layer_sizes=(128,64,32))
        }
        self.montecarlo_results = {}

    def most_frequent(self, iterable: list) -> object:
        occurence_count = Counter(iterable)
        return occurence_count.most_common(1)[0][0]

    def fit(self, dataset: pd.DataFrame,
            label_names: list = ['label', 'sublabel']) -> None:
        for i in range(self.pred_iteration):
            dataset = dataset.sample(frac=1)
            train, test = train_test_split(
                dataset, test_size=self.split_ratio)
            for model in self.classification_models.keys():
                self.classification_models[model].fit(train.drop(
                    label_names, axis=1), train[label_names[0]])
                pred = self.classification_models[model].predict_proba(
                    test.drop(label_names, axis=1))
                classes = self.classification_models[model].classes_
                try:
                    pred_labels = [(test_i, classes[i]) for i, pred_values, test_i in zip(
                    np.argmax(pred, axis=0), pred, test.index) if pred_values[i] > self.pred_threshold]
                except:
                    print(pred)
                for key, value in pred_labels:
                    if key not in self.montecarlo_results:
                        self.montecarlo_results[key] = [value]
                    else:
                        self.montecarlo_results[key].append(value)

    def transform(self, dataset: pd.DataFrame,
                  label_names: list = ['label', 'sublabel']) -> pd.DataFrame:
        corrected_labels = {key: self.most_frequent(
            value) for key, value in self.montecarlo_results.items()}
        resulting_data = dataset.copy()
        for index, corrected_label in corrected_labels.items():
            resulting_data.loc[index, label_names[0]] = corrected_label
        return resulting_data

    # --- Main Function --- #
    def fit_transform(self, dataset: pd.DataFrame,
                      label_names: list = ['label', 'sublabel']) -> pd.DataFrame:
        for i in range(self.epoch):
            print(i)
            self.fit(dataset)
            dataset = self.transform(dataset)
            self.montecarlo_results = {}
            # should i renew the montecarlo results?
        return dataset
            
