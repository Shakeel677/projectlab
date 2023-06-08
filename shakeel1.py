import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
dataset=pd.read_csv('Documents/shakeel.csv')
dataset

label=LabelEncoder()
label.fit(dataset.sex.drop_duplicate())
dataset.sex=label.transform(dataset.sex)
label.fit(dataset.smoker.drop_duplicate())
dataset.smoker=label.transform(dataset.smoker)
label.fit(dataset.region.drop_duplicate())
dataset.region=label.transform(dataset.region)
dataset


Linear_model=LinearRegression()
Linear_model.fit(X_lin_train,y_lin_train)

pred=Linear_model.predict(X_lin-test)
pred

linear_model.score(X_lin_test,pred)


for idx,col_name in enumerate(X_lin-train.columns):
      print("the coeffcient for {}is {}".format(col_name,Linear_model.coef_[0][idx]))
intercept=Linear_model.intercept_[0]
intercept
