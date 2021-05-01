def report_classification(df_features,df_target,algorithms='default',test_size=0.3,scaling=None,
                          large_data=False,encode='dummy',average='binary',change_data_type = False,
                          threshold=8,random_state=None):
    '''
    
    df_features : Pandas DataFrame
    
    df_target : Pandas Series
    
    algorithms : List ,'default'=
                 [LogisticRegression(),
                 GaussianNB(),
                 DecisionTreeClassifier(),
                 RandomForestClassifier(),
                 GradientBoostingClassifier(),
                 AdaBoostClassifier(),
                 XGBClassifier()]
                 The above are the default algorithms, if one needs any specific algorithms, they have to import
                 libraries then pass the instances of alogorith as list
                 For example, if one needs random forest and adaboost only, then pass 
                 
                 algorithms=[RandomForestClassifier(max_depth=8),AdaBoostClassifier()]
                 But, these libraries must be imported before passing into above list like
                 
    
    test_size: If float, should be between 0.0 and 1.0 and represent the proportion of the 
               dataset to include in the test split.
    
    scaling : {'standard-scalar', 'min-max'} or None , default=None
    
    encode : {'dummy','onehot','label'} ,default='dummy'
    
    change_data_type : bool, default=False
                       Some columns will be of numerical datatype though there are only 2-3 unique values in that column,
                       so these columns must be converted to object as it is more relevant.
                       By setting change_data_type= True , these columns will be converted into object datatype
    
    threshold : int ,default=8
                Maximum unique value a column can have
    
    large_data : bool, default=False
                If the dataset is large then the parameter large_data should be set to True, 
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
        
    random_state : int, RandomState instance or None, default=None
    
    '''
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report,confusion_matrix,roc_auc_score,roc_curve,accuracy_score,recall_score,precision_score
    from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from xgboost import XGBClassifier
    from warnings import filterwarnings
    filterwarnings('ignore')
    
    print("Shape of the data :",df_features.shape)
    print("---------------------------------------")
    
    #Check if there is any missing values
    if df_features.isna().sum().sum()==0:
        df_num=df_features.select_dtypes(exclude="object")
        #Some columns will be of numerical datatype though there are only 2-3 unique values in that column
        #Here the if-condition will check if the unique values are less than the specified threshold in each column
        if change_data_type == True:
            for i in df_num.columns:
                if len(df_num[i].value_counts())<threshold:
                    #The datatype will be changed to object if the condition is not satisfied
                    df_features[i] = df_features[i].astype('object')
                    print("Datatype of {} changed to 'object as there were less than {} unique values".format(i,threshold))
                    print("-----------------------------------------------------------------------------------------")
       
        else:
            pass
        #In some features like movie-tiltle,id,etc where there will be many unique values must be must be dropped
        #These features can also be label encoded and then can be passed
        df_cat=df_features.select_dtypes(include="object")
        for i in df_cat:
            if df_features[i].nunique()>threshold:
                raise Exception("Recheck the datatype of {}, as there are more than {} unique values or change the datatype of {}".format(i,threshold))
                
                
        df_num=df_features.select_dtypes(exclude="object")

        
        #Encoding of categorical features
        if df_cat.shape[1]!=0:
            #Dummy-encoding
            if encode == 'dummy':
                print("Encoding : Dummy Encoding" )
                print("---------------------------------------")
                encoding=pd.get_dummies(df_cat,drop_first=True)
                X=pd.concat([encoding,df_num],axis=1)
            #Onehot encoding
            elif encode == 'onehot':
                print("Encoding : One-hot Encoding" )
                print("---------------------------------------")
                encoding=pd.get_dummies(df_cat)
                X=pd.concat([encoding,df_num],axis=1)
            #Label encoding
            elif encode == 'label':
                print("Encoding : Label Encoding" )
                print("---------------------------------------")
                encoding=df_cat.apply(LabelEncoder().fit_transform)
                X=pd.concat([encoding,df_num],axis=1)
        #If there are no categorical features
        else:
            X=df_features
         
        
        #Encoding of target column
        labelencoder = LabelEncoder()
        y = labelencoder.fit_transform(df_target)
        
        #Value count of target column
        count=pd.Series(y).value_counts()
        print("Value count of target variable :")
        for i in range(len(count)):
            print("Count of {}s is {} ".format(count.index[i],count.values[i]))
        print("---------------------------------------")

        #Scaling
        #Standard scaling
        if scaling=='standard-scalar':
            print("Scaling : StandardScalar")
            print("---------------------------------------")
            ss=StandardScaler()
            X=ss.fit_transform(X)
        #MinmaxScalar
        elif scaling=='min-max':
            print("Scaling : MinmaxScalar")
            print("---------------------------------------")
            mm=MinMaxScaler()
            X=mm.fit_transform(X)
        else:
            print("Scaling : None")
            print("---------------------------------------")
            
            
        #Condition to check how large the data after encoding
        if (X.shape[0]*X.shape[1] < 1000000) | large_data==True:
            print("Number of Datapoints :",X.shape[0]*X.shape[1])
            print("---------------------------------------")
        else:
            raise Exception("Data too large to process, if you want to still execute, set parameter large_data=False")
          

        #Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        print("Test size for train test split :",test_size)
        print("---------------------------------------")
        
        #Algorithms
        if algorithms == 'default':
            
            algorithms=[LogisticRegression(),
                        GaussianNB(),
                        DecisionTreeClassifier(random_state=random_state),
                        RandomForestClassifier(random_state=random_state),
                        GradientBoostingClassifier(random_state=random_state),
                        AdaBoostClassifier(random_state=random_state),
                       XGBClassifier(random_state=random_state,verbosity=0)]
        else: 
            algorithms=algorithms
            
        
            
        
        #Binary Classification
        if df_target.nunique()<3:
            
            results=pd.DataFrame(columns=["Algorithm_name",'Train_accuracy','Test_accuracy',
                                          "Test_Roc_Auc_score",'Test_recall','Test_precision'])
            for i in algorithms:
                print("Executing :",i)
                i.fit(X_train, y_train)
                train_pred_i=i.predict(X_train)
                train_acc=accuracy_score(y_train,train_pred_i)
                test_pred_i=i.predict(X_test)
                test_acc=accuracy_score(y_test,test_pred_i)
                recall=recall_score(y_test,test_pred_i,average=average)
                precision=precision_score(y_test,test_pred_i,average=average)
                roc_auc=roc_auc_score(y_test,test_pred_i)
                row={"Algorithm_name":str(i)[:-2],'Train_accuracy':train_acc,"Test_accuracy":test_acc,
                     "Test_Roc_Auc_score":roc_auc,'Test_recall':recall,"Test_precision":precision}
                results=results.append(row,ignore_index=True)
            return results
        
        #Multiclass Classification
        else:
            results=pd.DataFrame(columns=["Algorithm_name",'Train_accuracy','Test_accuracy',"f1_score"])
            for i in algorithms:
                print("Executing :",i)

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

        

def report_regression(df_features,df_target,algorithms='default',test_size=0.3,
                      scaling=None,large_data=False,change_data_type=True,encode='dummy',
                      threshold=8,random_state=None):
    '''

    df_features : Pandas DataFrame
    
    df_target : Pandas Series
    
     algorithms : List ,'default'=
                 [LinearRegression(),
                 Lasso(),
                 Ridge(),
                 RandomForestRegressor(),
                 GradientBoostingRegressor(),
                 AdaBoostRegressor(),
                 XGBRegressor]
                 The above are the default algorithms, if one needs any specific algorithms, they have to import
                 libraries then pass the instances of alogorith as list
                 For example, if one needs random forest and adaboost only, then pass 
                 
                 algorithms=[RandomForestRegressor(max_depth=8),AdaBoostRegressor()]
                 But, these libraries must be imported before passing into above list like
                 
    test_size: If float, should be between 0.0 and 1.0 and represent the proportion of the 
               dataset to include in the test split.
    
    scaling : {'standard-scalar', 'min-max'} or None , default=None
    
    encode : {'dummy','onehot','label'} ,default='dummy'
    
    change_data_type : bool, default=False
                       Some columns will be of numerical datatype though there are only 2-3 unique values in that column,
                       so these columns must be converted to object as it is more relevant.
                       By setting change_data_type= True , these columns will be converted into object datatype
    
    threshold : int ,default=8
                Maximum unique value a column can have
                
    large_data : bool, default=False
                If the dataset is large then the parameter large_data should be set to True, 
                make sure if your system has enough memory before setting Large_data=True
                
    random_state : int, RandomState instance or None, default=None
    
    '''
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.linear_model import LinearRegression,Lasso,Ridge
    from xgboost import XGBRegressor
    from warnings import filterwarnings
    filterwarnings('ignore')
    print("Shape of data :",df_features.shape)
    print("---------------------------------------")
    
    #Check if there is any missing values
    if df_features.isna().sum().sum()==0:
        
        df_num=df_features.select_dtypes(exclude="object")
        #Some columns will be of numerical datatype though there are only 2-3 unique values in that column
        #Here the if-condition will check if the unique values are less than the specified threshold in each column
        if change_data_type == True:
            for i in df_num.columns:
                #The datatype will be changed to object if the condition is not satisfied
                if len(df_num[i].value_counts())<threshold:
                    df_features[i] = df_features[i].astype('object')
                    print("Datatype of {} changed to 'object as there were less than {} unique values".format(i,threshold))

            print("-----------------------------------------------------------------------------------------")
        else:
            pass
        
        #In some features like movie-tiltle,id,etc where there will be many unique values must be must be dropped
        #These features can also be label encoded and then can be passed
        df_cat=df_features.select_dtypes(include="object")
        for i in df_cat:
            if df_features[i].nunique()>threshold:
                raise Exception("Recheck the datatype of {}, as there are more than {} unique values or change the datatype of {}".format(i,threshold))
                
                
        df_num=df_features.select_dtypes(exclude="object")
        #Encoding of categorical features
        if df_cat.shape[1]!=0:
            #Dummy Encoding
            if encode == 'dummy':
                print("Encoding : Dummy Encoding" )
                print("---------------------------------------")
                encoding=pd.get_dummies(df_cat,drop_first=True)
                X=pd.concat([encoding,df_num],axis=1)
            #Onehot encoding
            elif encode == 'onehot':
                print("Encoding : One-hot Encoding" )
                print("---------------------------------------")
                encoding=pd.get_dummies(df_cat)
                X=pd.concat([encoding,df_num],axis=1)
            #Label encoding
            elif encode == 'label':
                print("Encoding : Label Encoding" )
                print("---------------------------------------")
                encoding=df_cat.apply(LabelEncoder().fit_transform)
                X=pd.concat([encoding,df_num],axis=1)  
        else:
           
            X=df_features
        
        #Encoding of target column
        labelencoder = LabelEncoder()
        y = labelencoder.fit_transform(df_target)
        
    
        #Scaling
        #Scaling of features by StandardScalar
        if scaling=='standard-scalar':
            print("Scaling : standardScalar")
            print("---------------------------------------")
            ss=StandardScaler()
            X=ss.fit_transform(X)
        #Scaling of features by MinmaxScalar
        elif scaling=='min-max':
            print("Scaling : inmaxScalar")
            print("---------------------------------------")
            mm=MinMaxScaler()
            X=mm.fit_transform(X)
        else:
            print("Scaling : None")
            print("---------------------------------------")
        
        #Condition to check how large the data after encoding
        if (X.shape[0]*X.shape[1] < 1000000) | large_data==True:
            print("Number of Datapoints :",X.shape[0]*X.shape[1])
            print("---------------------------------------")
        else:
            raise Exception("Data too large to process, if you want to still execute, set parameter large_data=False")
          

        #Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,random_state=random_state)
        print("Test size for train test split :",test_size)
        print("---------------------------------------")

        if algorithms == 'default':
            
            algorithms=[LinearRegression(),
                        Lasso(random_state=random_state),
                        Ridge(random_state=random_state),
                        DecisionTreeRegressor(random_state=random_state),
                        RandomForestRegressor(random_state=random_state),
                        GradientBoostingRegressor(random_state=random_state),
                        AdaBoostRegressor(random_state=random_state),
                        XGBRegressor(random_state=random_state)]
        else: 
            algorithms=algorithms

        results=pd.DataFrame(columns=["Algorithm_name",'R-Squared','Adj. R-Squared','Train-RMSE','Test-RMSE'])
        for i in algorithms:
            print("Executing :",i)
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
            row={"Algorithm_name":str(i)[:-2],'R-Squared':r_sq,'Adj. R-Squared':ad_r_sq,
                 'Train-RMSE':rmse_train,'Test-RMSE':rmse_test}
            results=results.append(row,ignore_index=True)
            
        return results

    else:
        raise Exception("The data contains missing values, first handle missing values and then pass the data")

        
        
