import joblib
from trees import ProximityForest
from core import FileReader
import sys

sys.path.append("/Users/morad/PycharmProjects/PForests/")  # TODO: CHANGE
# sys.path.append(sys.argv[1])
import time
import timeit
from datetime import date
from core import AppContext, ExperimentRunner
import json

train_dataset = FileReader.FileReader.load_arff_data(
    "/Users/morad/PycharmProjects/PForests/datasets/Chinatown/Chinatown_TRAIN.arff")
test_dataset = FileReader.FileReader.load_arff_data(
    "/Users/morad/PycharmProjects/PForests/datasets/Chinatown/Chinatown_TEST.arff")

model = ProximityForest.ProximityForest(1, n_trees=20, n_candidates=5)
filename = 'pf_model.sav'

model.train(train_dataset)
results = model.test(test_dataset)
joblib.dump(model, filename)
print(results.accuracy)

loaded_model = joblib.load(filename)
predicted = loaded_model.predict(test_dataset.series_data[3])
print(predicted)

"""


class ScenarioOne:
    query_file = ""
    type = 1
    time_start = 0
    time_stop = 0
    train_dataset = ''
    AppContext.AppContext.output_dir = "../outputs/"
    dt_name = ''

    def get_args(self):
        if len(sys.argv) > 1:
            for i in range(2, len(sys.argv)):
                options = sys.argv[i].split("=")
                arg = options[0]
                value = options[1]
                if arg == "-name":
                    self.dt_name = value
                elif arg == "-syspath":
                    sys.path.append(value)
                elif arg == "-train":
                    self.train_dataset = value

    @staticmethod
    def read_query_path(query):
        with open(query, 'r') as f:
            x = f.readlines()
        f.close()
        return x

    pass


# sys.path.append("/Users/morad/PycharmProjects/PForests/")  # TODO: CHANGE
scenario = ScenarioOne()
scenario.get_args()
model = ProximityForest(1, n_trees=20, n_candidates=2)


train_dataset = FileReader.FileReader.load_arff_data(scenario.train_dataset)
filename = '../mlexports/pf_' + scenario.dt_name + '_model.sav'
print(filename)
model.train(train_dataset)
joblib.dump(model, filename)

"""
