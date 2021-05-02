import timeit
import sys
import json
import time
sys.path.append(".")
import dtaidistance.dtw as dtw
import trees.ProximityForest as pf
import core.FileReader as reader
from sktime.classification.distance_based import _proximity_forest as pfsk
from sktime.utils.load_data import load_from_tsfile_to_dataframe as ts_loader
from sktime.utils.load_data import load_from_arff_to_dataframe as arff_loader
from sktime.distances.elastic import dtw_distance
import random
from sktime.classification.distance_based._proximity_forest import ProximityForest, ProximityStump, ProximityTree

#sys.path.append(sys.argv[1])


class PFSktime:
    name = ''
    training_path = None
    testing_path = None
    trees = 20
    candidates = 2
    jobs = 1

    def save_json(self, total_time, time_train, time_test, accuracy):
        f_path = '../outputs/sktime_' + self.name + '_results_' + str(
            time.localtime().tm_hour) + str(time.localtime().tm_min) + str(
            time.localtime().tm_sec) + ".json"
        data = {'dataset': []}
        data['dataset'].append({
            'name': self.name,
            'exec_time': total_time,
            'training_time': time_train,
            'testing_time': time_test,
            'accuracy': accuracy,
            'n_jobs': self.jobs
        })
        with open(f_path, 'w+') as file:
            file.write(json.dumps(data))
        file.close()
        return

    def get_args(self):
        if len(sys.argv) > 1:
            for i in range(2, len(sys.argv)):
                options = sys.argv[i].split("=")
                arg = options[0]
                value = options[1]
                if arg == "-name":
                    self.name = value
                elif arg == "-train":
                    self.training_path = value
                elif arg == "-test":
                    self.testing_path = value
                elif arg == "-jobs":
                    self.jobs = int(value)
                elif arg == "-trees":
                    self.trees = int(value)
                elif arg == "-candidates":
                    self.candidates = int(value)



pass

data_train = None
data_test = None

pfsktime = PFSktime()
pfsktime.get_args()
random.seed(1234)


# PROXIMITY FOREST

name = ''
training_path = '/Users/morad/Desktop/TSdatasets/ItalyPowerDemand/ItalyPowerDemand_TRAIN.arff'
testing_path = '/Users/morad/Desktop/TSdatasets/ItalyPowerDemand/ItalyPowerDemand_TEST.arff'
trees = 100
candidates = 5
jobs = 1

# pf_train = arff_loader(training_path);

pforest_sktime = pfsk.ProximityForest(n_estimators=trees,
                                                 n_stump_evaluations=candidates, n_jobs=jobs, distance_measure=dtw.distance_fast)

data_train = arff_loader(training_path)
data_test = arff_loader(testing_path)
start = timeit.default_timer()
train_time_start = timeit.default_timer()
X, y = pfsk.check_X_y(data_train[0], data_train[1], enforce_univariate=True)
pforest_sktime.fit(X, y)
train_time_stop = timeit.default_timer()

test_time_start = timeit.default_timer()
X_test, y_test = pfsk.check_X_y(data_test[0], data_test[1], enforce_univariate=True)
predictions = pforest_sktime.score(data_test[0], data_test[1])
preds = pforest_sktime.predict_proba(data_test[0])
print(preds[0])
test_time_stop = timeit.default_timer()

stop = timeit.default_timer()
print("[PForest Sktime] accuracy:", predictions)
print("[PForest Sktime] exec time:", stop - start)

# pforest.predict_proba()

