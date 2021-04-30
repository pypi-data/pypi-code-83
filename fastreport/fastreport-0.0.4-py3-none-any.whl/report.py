def report_classification(df_features,df_target,test_size=0.3,scaling=False,large_data=False,average='binary'):
    '''

    df_features: Pandas DataFrame
    df_target: Pandas Series
    test_size: If float, should be between 0.0 and 1.0 and represent the proportion of the 
               dataset to include in the test split.
    scaling: Scaling(Standaed scalar) of the features if scaling is set to True
    large_data: If the dataset is large then the parameter large_data should be set to True, 
                make sure if your system has enough memory before setting Large_data=True
    average : {'micro', 'macro', 'samples','weighted', 'binary'} or None, default='binary'
    This parameter is required for multiclass/multilabel targets.
    If ``None``, the scores for each class are returned. Otherwise, this
    determines the type of averaging performed on the data:

    ``'binary'``:
        Only report results for the class specified by ``pos_label``.
        This is applicable only if targets (``y_{true,pred}``) are binary.
    ``'micro'``:
        Calculate metrics globally by counting the total true positives,
        false negatives and false positives.
    ``'macro'``:
        Calculate metrics for each label, and find their unweighted
        mean.  This does not take label imbalance into account.
    ``'weighted'``:
        Calculate metrics for each label, and find their average weighted
        by support (the number of true instances for each label). This
        alters 'macro' to account for label imbalance; it can result in an
        F-score that is not between precision and recall.
    ``'samples'``:
        Calculate metrics for each instance, and find their average (only
        meaningful for multilabel classification where this differs from
        :func:`accuracy_score`).
    
    '''
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder,StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report,confusion_matrix,roc_auc_score,roc_curve,accuracy_score,recall_score,precision_score
    from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from warnings import filterwarnings
    filterwarnings('ignore')
    if df_features.isna().sum().sum()==0:
        df_cat=df_features.select_dtypes(include="object")
        for i in df_cat:
            if df_features[i].nunique()>10:
                raise Exception("Recheck the datatype of {}, as there are more than 10 unique values or change the datatype of {}".format(i,i))
                
                
        df_num=df_features.select_dtypes(exclude="object")
        if df_cat.shape[1]!=0:
            encoding=pd.get_dummies(df_cat,drop_first=True)
            X=pd.concat([encoding,df_num],axis=1)
        else:
            X=df_features
        labelencoder = LabelEncoder()
        y = labelencoder.fit_transform(df_target)
        if scaling==True:
            ss=StandardScaler()
            X=ss.fit_transform(X)
        else:
            pass
        if (X.shape[0]*X.shape[1] < 1000000) | large_data==True:
            print("Number of Datapoints:",X.shape[0]*X.shape[1])
        else:
            raise Exception("Data too large to process, if you want to still execute, set parameter large_data=False")
          


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        algo=[LogisticRegression(),GaussianNB(),DecisionTreeClassifier(),RandomForestClassifier(),
              GradientBoostingClassifier(),AdaBoostClassifier()]
       
        if df_target.nunique()<3:
            print("Class: Binary")
            
            results=pd.DataFrame(columns=["Algorithm_name",'Train_accuracy','Test_accuracy',"Test_Roc_Auc_score",'Test_recall','Test_precision'])
            for i in algo:

                i.fit(X_train, y_train)
                train_pred_i=i.predict(X_train)
                train_acc=accuracy_score(y_train,train_pred_i)
                test_pred_i=i.predict(X_test)
                test_acc=accuracy_score(y_test,test_pred_i)
                recall=recall_score(y_test,test_pred_i,average=average)
                precision=precision_score(y_test,test_pred_i,average=average)
                roc_auc=roc_auc_score(y_test,test_pred_i)
                row={"Algorithm_name":str(i)[:-2],'Train_accuracy':train_acc,"Test_accuracy":test_acc,"Test_Roc_Auc_score":roc_auc,'Test_recall':recall,"Test_precision":precision}
                results=results.append(row,ignore_index=True)
            return results
        else:
            print("Class: Multiclass")
            results=pd.DataFrame(columns=["Algorithm_name",'Train_accuracy','Test_accuracy',"f1_score"])
            for i in algo:

                i.fit(X_train, y_train)
                train_pred_i=i.predict(X_train)
                train_acc=accuracy_score(y_train,train_pred_i)
                test_pred_i=i.predict(X_test)
                test_acc=accuracy_score(y_test,test_pred_i)
                f1=recall_score(y_test,test_pred_i,average=average)
                
                row={"Algorithm_name":str(i)[:-2],'Train_accuracy':train_acc,"Test_accuracy":test_acc,"f1_score":f1}
                results=results.append(row,ignore_index=True)
            return results
            
    else:
        raise Exception("The data contains missing values, first handle missing values and then pass the data")

        

def report_regression(df_features,df_target,test_size=0.3,scaling=False,large_data=False):
    '''

    df_features: Pandas DataFrame
    df_target: Pandas Series
    test_size: If float, should be between 0.0 and 1.0 and represent the proportion of the
               dataset to include in the test split.
    scaling: Scaling(Standaed scalar) of the features if scaling is set to True
    
    '''
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder,StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.linear_model import LinearRegression,Lasso,Ridge
    from warnings import filterwarnings
    filterwarnings('ignore')
    if df_features.isna().sum().sum()==0:
        df_cat=df_features.select_dtypes(include="object")
        for i in df_cat:
            if df_features[i].nunique()>10:
                raise Exception("Recheck the datatype of {}, as there are more than 10 unique values or change the datatype of {}".format(i,i))
                
                
        df_num=df_features.select_dtypes(exclude="object")
        if df_cat.shape[1]!=0:
            encoding=pd.get_dummies(df_cat,drop_first=True)
            X=pd.concat([encoding,df_num],axis=1)
        else:
            X=df_features
        labelencoder = LabelEncoder()
        y = labelencoder.fit_transform(df_target)
        if scaling==True:
            ss=StandardScaler()
            X=ss.fit_transform(X)
        else:
            pass
        if (X.shape[0]*X.shape[1] < 1000000) | large_data==True:
            print("Number of Datapoints:",X.shape[0]*X.shape[1])
        else:
            raise Exception("Data too large to process, if you want to still execute, set parameter large_data=False")
          


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        algo=[LinearRegression(),Lasso(),Ridge(),DecisionTreeRegressor(),RandomForestRegressor(),
              GradientBoostingRegressor(),AdaBoostRegressor()]
        results=pd.DataFrame(columns=["Algorithm_name",'R-Squared','Adj. R-Squared','Train-RMSE','Test-RMSE'])
        for i in algo:
            i.fit(X_train, y_train)
            train_pred_i=i.predict(X_train)
            n = X_train.shape[0]
            k = X_train.shape[1]
            r_sq=i.score(X_train, y_train)
            ad_r_sq=1 -((1-r_sq)*(n-1)/(n-k-1))
            test_pred_i=i.predict(X_test)
            
            mse_train = mean_squared_error(y_train, train_pred_i)
            rmse_train = round(np.sqrt(mse_train), 4)
        
            mse_test = mean_squared_error(y_test, test_pred_i)
            rmse_test = round(np.sqrt(mse_test), 4)
        
            #test_r_sq=i.score(y_test,test_pred_i)
            row={"Algorithm_name":str(i)[:-2],'R-Squared':r_sq,'Adj. R-Squared':ad_r_sq,'Train-RMSE':rmse_train,'Test-RMSE':rmse_test}
            results=results.append(row,ignore_index=True)
        return results
    else:
        raise Exception("The data contains missing values, first handle missing values and then pass the data")

        
        
        
