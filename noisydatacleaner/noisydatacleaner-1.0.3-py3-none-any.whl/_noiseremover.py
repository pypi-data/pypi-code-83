import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

class NoiseRemover:
    def __init__(self, threshold: int = 0.6):
        self.threshold = threshold
    
    def set_threshold(self: None, threshold_value: int) -> None:
        self.threshold = threshold_value
    
    def detect_noise(self: None,
                     X: pd.DataFrame,
                     y: pd.Series,
                     method: str = 'rf') -> np.ndarray:
        if method == 'rf':
            rf = RandomForestClassifier(oob_score=True).fit(X, y)
            noise_prob = 1 - rf.oob_decision_function_[range(len(y)), y]
            return np.argwhere(noise_prob > self.threshold).reshape(-1)
        elif method == 'knn':
            knn = KNeighborsClassifier().fit(X, y)
            noise_prob = 1 - knn.predict_proba(X)[range(len(X)), y]
            return np.argwhere(noise_prob > self.threshold).reshape(-1)
        else:
            raise AttributeError('Method not recognized. Choose \{rf, knn\}')
    
    def labelfilter_noisy_indexes(noisy_indexes: np.ndarray,
                                data: pd.DataFrame,
                                label: str) -> np.ndarray:
        noisy_data = data.loc[noisy_indexes]
        return noisy_data.loc[noisy_data.label == label, :].index

    # --- Main Function --- #
    def remove_noise(self: None,
                        X: pd.DataFrame,
                        y: pd.Series) -> pd.DataFrame:
        unique_labels = y.unique()
        n_labels = len(unique_labels)
        data = X.copy()
        data['label'] = y
        if n_labels == 2:
            key_label = unique_labels[0]
            new_y = y.apply(lambda x: 1 if x == key_label else 0)
            noisy_indexes = self.detect_noise(
                data.drop('label', axis=1), new_y)
            clean_noisy_indexes = self.labelfilter_noisy_indexes(
                noisy_indexes, data, key_label)
            return data.loc[data.index.difference(clean_noisy_indexes)]
        else:
            all_noisy_indexes = np.array([])
            for key_label in unique_labels:
                new_y = y.apply(lambda x: 1 if x == key_label else 0)
                noisy_indexes = self.detect_noise(
                    data.drop('label', axis=1), new_y)
                clean_noisy_indexes = self.labelfilter_noisy_indexes(
                    noisy_indexes, data, key_label
                )
                all_noisy_indexes = np.append(
                    all_noisy_indexes, clean_noisy_indexes)
            return data.loc[data.index.difference(all_noisy_indexes)]