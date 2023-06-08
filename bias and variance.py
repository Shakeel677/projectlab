import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
from sklearn.linear_ model import LinearRegression,Lesso
import datetime
from ststistics import mean
data["Date"]=pd.to-datetime(data["formatted date"],utc=True)
data["Month"]=data["Date"].dt.month
data
data=data.drop(['formatted date','daily summary','pressure'],axis=1)
data

label_encoder=preprocessing.LabelEncoder()
data['summary']=label_encoder.fit_transform(data['summary'])
data['summary'].unique()
data
                                        
