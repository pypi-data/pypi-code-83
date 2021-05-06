import pandas as pd
import numpy as np
from scipy import stats
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer #SimpleImputer
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression#LogisticRegression
from sklearn.svm import SVC#SVC
from sklearn.svm import SVR
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier #RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier#GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest #SelectKBest
from sklearn.impute import KNNImputer #KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics


def getHyperparams(model):
    '''Return a dictionary of hypermparameters based on the model
        Params:
        ML model
        If model has not hyperparams return a message: 'No params available'
    '''

    if type(model).__name__ == 'LogisticRegression':

        return {                   
                "penalty": ["l1","l2"], 
                "C": [0.1, 0.5, 1.0, 5.0],
                "max_iter": [50,100,500],   
                "solver": ["liblinear"]
                }

    # elif type(model).__name__=='KNN':
    #     return {"n_neighbors": [3,5,7,9,11], 
    #               "weights": ["uniform","distance"] 
    #             }

    # elif type(model).__name__== 'DecissionTree':?
    #     return {"max_depth":list(range(1,10)) 
    #           }
    elif type(model).__name__=='RandomForestClassifier':

        return {"n_estimators": [120],
                "max_depth": [3,4,5,6,10,15,17],
                "max_features": ["sqrt", 3, 4]
                }

    elif type(model).__name__=='SVC':

        return {"C": [0.01, 0.1, 0.3, 0.5, 1.0, 3, 5.0, 15, 30],
            "kernel": ["linear","poly","rbf"],
            "degree": [2,3,4,5], 
            "gamma": [0.001, 0.1, "auto", 1.0, 10.0, 30.0]
           }
    
    elif type(model).__name__=="SVR":
        return {"kernel":["linear","poly","rbf"],
                "degree":[2,3,4,5], 
                "C":[0.3, 0.5, 1.0, 3, 5.0, 15, 30,100],
                "epsilon":[0.1], 
                "gamma":["auto","scale"]
                }
    elif type(model).__name__=='GradientBoostingClassifier':
        
        return {"loss": ["deviance"],
                "learning_rate": [0.05, 0.1, 0.2, 0.4, 0.5],
                "n_estimators": [20,50,100,200],
                "max_depth": [1,2,3,4,5],
                "max_features": ["sqrt", 3, 4],
                }
    # elif type(model).__name__=='XgBoost':?
    #     return {
    #             "learning_rate": [0.05, 0.1, 0.2, 0.4, 0.5],
    #             "n_estimators": [20,50,100,200],
    #             "max_depth": [1,2,3,4,5]
    #             }

    else:
        return "No params available"

def createSearchSpaces(modelList):
    search_spaces = []
    for model in modelList:
        params = getHyperparams(model)

#Función para regresión lineal 

# def train_pred_linear(X, y, test_size, random_state, n_jobs):
    
#     X_train, X_test, y_train, y_test = train_test_split(X, 
#                                                         y, 
#                                                         test_size=test_size, 
#                                                         random_state=random_state)
    
#     lm = LinearRegression(n_jobs=n_jobs)    
#     lm.fit(X_train, y_train)
#     predictions = lm.predict(X_test)
    
#     print('lm_intercept_', lm.intercept_)
#     print('lm.coef_', lm.coef_)    
    
#     coeff_df = pd.DataFrame(lm.coef_,
#                        X_train.columns,
#                        columns = ['Coefficent'])
    
#     print('MAE', metrics.mean_absolute_error(y_test, predictions))
#     print('MSE', metrics.mean_squared_error(y_test, predictions))
#     print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
#     print('lm_train', lm.score(X_train, y_train))
#     print('lm_test', lm.score(X_test, y_test))
    
#     return coeff_df, predictions

def linearRegressionModel(X, y, test_size=0.2, random_state=42, n_jobs=1,std_scal=False, poly_degree=1):
    '''
    Apply LinearRegression or Polynomial model
    Params:
    X whole set of features
    y whole set of targets
    test_size size of test default=0.2
    random_state seed default=42
    n_jobs number of cores default=1
    std_scal boolean apply standar scaler or not default = False
    poly_degree degree for polynomial transform, only apply if degree > 1 default=1
    Return ....?????
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=test_size, 
                                                        random_state=random_state)
    if std_scal:
        X_train, X_test = applyStdScaler(X_train,X_test)
        # std_scale = StandardScaler()
        # std_scale.fit(X_train)
        # X_train = std_scale.transform(X_train)
        # X_test = std_scale.transform(X_test)

    if poly_degree >1:
        X_train, X_test = applyPolynomialFeature(X_train,X_test,poly_degree)
        # poly_reg = PolynomialFeatures(degree = poly_degree)
        # poly_reg.fit(X_train)
        # X_train = poly_reg.transform(X_train)
        # X_test = poly_reg.transform(X_test)


    lm = LinearRegression(n_jobs=n_jobs)
    lm.fit(X_train, y_train)

    
    predictions = lm.predict(X_test)
    
    print ('lm_scal.intercept_', lm.intercept_)
    print ('lm_scal.coef_', lm.coef_)    
    
    coeff_df = pd.DataFrame(lm.coef_,
                       X_train.columns,
                       columns = ['Coefficent'])
    
    print('MAE', metrics.mean_absolute_error(y_test, predictions))
    print('MSE', metrics.mean_squared_error(y_test, predictions))
    print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
    print('lm_scal_train', lm.score(X_train, y_train))
    print('lm_scal_test', lm.score(X_test, y_test))    
    
    return coeff_df, predictions  


def applyPolynomialFeature(X_train,X_test,degree):
    '''
    transform using polynomial feature
    params:
    X_train train set
    X_test test set
    degree of polynomial
    Return:
    Transform (X_train, X_test)
    '''

    poly_reg = PolynomialFeatures(degree = degree)
    poly_reg.fit(X_train)

    return poly_reg.transform(X_train),poly_reg.transform(X_test)

def applyStdScaler(X_train,X_test):
    '''
    transform using standard scaler
    params:
    X_train train set
    X_test test set
  
    Return:
    Transform (X_train, X_test)
    '''
    std_scale = StandardScaler()
    std_scale.fit(X_train)

    return std_scale.transform(X_train), std_scale.transform(X_test)

# if __name__=='__main__':
#     svm = SVC()
#     print(getHyperparams(svm))