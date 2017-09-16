import numpy as np
import pandas as pd
import sklearn as skl
import scipy as sc
from sklearn import preprocessing
from sklearn import svm

data = pd.read_csv("c://trainings//credit_train2.csv", encoding="UTF-8", sep=';')
test = pd.read_csv("c://trainings//credit_test2.csv", encoding="UTF-8", sep=';')
#print(data.head())
data.isnull().any()
data = data.fillna(lambda x: x.median())

test["education"] = pd.get_dummies(test['education'])
test["marital_status"] = pd.get_dummies(test['marital_status'])
test["job_position"] = pd.get_dummies(test['job_position'])
test["gender"] = pd.get_dummies(test['gender'])


data["education"] = pd.get_dummies(data['education'])
data["marital_status"] = pd.get_dummies(data['marital_status'])
data["job_position"] = pd.get_dummies(data['job_position'])
data["gender"] = pd.get_dummies(data['gender'])

del data['living_region']
#print(data[:15])
y = data['open_account_flg']
del data['open_account_flg']
X = data[["education", "age", "job_position", "marital_status"]]#, "credit_sum", "credit_month", "tariff_id", "monthly_income"]]

svm_model = svm.SVC()
svm_model.fit(X, y)
prediction = svm_model.predict(test[["education", "age", "job_position"]])

print(prediction)

