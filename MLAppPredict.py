import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import joblib

def bcprediction(a,b,c,d,e):
    breast=pd.read_csv('Breast_cancer_data.csv')
    X=breast.drop (columns=['diagnosis'])
    y=breast['diagnosis']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

    model=DecisionTreeClassifier()
    model.fit(X_train,y_train)

    prediction=model.predict([[a,b,c,d,e]])
    return prediction





