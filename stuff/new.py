import pandas as pd
import numpy as np
from sklearn import metrics, preprocessing
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv('c:\\trainings\\credit_train1.csv', sep=';', encoding='CP1251')
df_test = pd.read_csv('c:\\trainings\\credit_test1.csv', sep=';', encoding='CP1251')
#df = df.fillna(lambda x: x.median())
df.dropna()

parsable_columns = ['credit_sum', 'score_shk'] #, 'monthly_income', 'credit_count', 'overdue_credit_count']
for key in parsable_columns:
    df[key] = df[key].map(lambda val: val.replace(',','.')).map(float)
    df_test[key] = df_test[key].map(lambda val: val.replace(',','.')).map(float)

key = 'living_region'
df[key] = df[key].map(lambda val: str(val).replace(',','.'))
df_test[key] = df_test[key].map(lambda val: str(val).replace(',','.'))

categorizable_columns = ['gender', 'marital_status', 'job_position', 'education', 'living_region']
for key in categorizable_columns:
    le = preprocessing.LabelEncoder()
    le.fit(
        np.unique(
            np.concatenate((
                df[key].unique(),
                df_test[key].unique()
            ))
        )
    )
    df[key] = le.transform(df[key])
    df_test[key] = le.transform(df_test[key])

df_train = df
target = "open_account_flg"
X_train = df_train.drop(target, axis=1)
#X_train = df_train[df_train.drop(target, axis=1).columns]
Y_train = df_train[target]

gbc = GradientBoostingClassifier()
gbc.fit(X_train, Y_train)
r = gbc.predict_proba(df_test.drop([], axis=1))