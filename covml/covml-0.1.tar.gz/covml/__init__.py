from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


df = pd.read_csv('data/corona.csv', low_memory=False)

df.drop('test_date', axis=1, inplace=True)
df = pd.get_dummies(
    df, columns=['test_indication', 'corona_result', 'age_60_and_above', 'gender'])
df.drop('corona_result_negative', axis=1, inplace=True)
df.drop('corona_result_other', axis=1, inplace=True)

# TRAIN_TEST_SPLIT

X = df.drop('corona_result_positive', axis=1)
y = df['corona_result_positive']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=101)

# MODELLING AND STUFF

lm = LogisticRegression()
lm.fit(X_train, y_train)

# PREDICTIONS


def predict_cov19(has_cough=None,
                has_fever=None,
                has_shortness_of_breath=None,
                has_head_ache=None,
                has_been_abroad=None,
                contact_with_confirmed=None,
                other=0,
                above_60_yes=None,
                above_60_no=None,
                is_female=None,
                is_male=None,
                miscellaneous=0
                ):

    arr = np.array([has_cough,
                    has_fever,
                    has_shortness_of_breath,
                    has_head_ache,
                    has_been_abroad,
                    contact_with_confirmed,
                    other,
                    above_60_yes,
                    above_60_no,
                    is_female,
                    is_male,
                    miscellaneous]).reshape(1, -1)

    prediction = lm.predict(arr)

    return prediction[0]
