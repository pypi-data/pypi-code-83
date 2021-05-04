def train_val_test_split(X,y,val_size=0.15,test_size=0.15,shuffle=True):
    """
    Splits arrays or matrices into random train, validation and test subsets
    "train_val_test_split" function accepts independent features(X), dependent
    feature (y), validation size (default size = 0.15),test size (default size = 0.15)
    and shuffle (default = True) as input parameters and returns X_train,X_val,X_test,y_train,y_val,y_test
    
    Note: If shuffle parameter is True, after shuffling index of all records will be reset in ascending order
    
    How to use it:
    
    from vinzy_splitter import train_val_test_split
    
    X_train,X_val,X_test,y_train,y_val,y_test = train_val_test_split(X,y,val_size=0.15,test_size=0.15,shuffle=True)
    
    now your data frame will be splitted into training,validation and testting
    subsets based on validation and testing size you have provided, deafult value will be 15% for both
    and suffling will be True.
    """
    
    import pandas as pd
    if shuffle == True:
        df = pd.concat([X,y],axis=1)
        df = df.sample(frac=1).reset_index(drop=True)
        X = df.iloc[:,:-1]
        y = df.iloc[:,-1]
        val_chunk = int(len(df)*val_size)
        test_chunk = int(len(df)*test_size)
        X_val,y_val = X.iloc[:val_chunk,:],y[:val_chunk]
        X_test,y_test = X.iloc[val_chunk:val_chunk+test_chunk,:],y[val_chunk:val_chunk+test_chunk]
        X_train,y_train = X.iloc[val_chunk+test_chunk:,:],y[val_chunk+test_chunk:]
        return X_train,X_val,X_test,y_train,y_val,y_test
    else:
        df = pd.concat([X,y],axis=1)
        X = df.iloc[:,:-1]
        y = df.iloc[:,-1]
        val_chunk = int(len(df)*val_size)
        test_chunk = int(len(df)*test_size)
        X_val,y_val = X.iloc[:val_chunk,:],y[:val_chunk]
        X_test,y_test = X.iloc[val_chunk:val_chunk+test_chunk,:],y[:val_chunk+test_chunk]
        X_train,y_train = X.iloc[val_chunk+test_chunk:,:],y[val_chunk+test_chunk:]
        return X_train,X_val,X_test,y_train,y_val,y_test



def author():
    """
    Returns Author's Name
    """
    return "Package written by Vinayak Bhosale"