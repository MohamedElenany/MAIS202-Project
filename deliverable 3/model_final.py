import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from scipy import stats


def proccess_data(data):
    res = []
    res.append(data[0])
    if (data[1] == "Male"):
        res.append(1)
    else:
        res.append(0)
    res.append(data[3])
    res.append(data[4])
    if (data[5] == "fbs_true"):
        res.append(1)
    else:
        res.append(0)
    res.append(data[7])
    if (data[8] == "exang_true"):
        res.append(1)
    else:
        res.append(0)
    res.append(data[9])
    res.append(float(data[11]))
    if (data[6] == "lv hypertrophy"):
        res.extend([1,0,0])
    elif (data[6] == "normal"):
        res.extend([0,1,0])
    else:
        res.extend([0,0,1])

    if (data[2] == "asymptomatic"):
        res.extend([1,0,0,0])
    elif (data[2] == "atypical angina"):
        res.extend([0,1,0,0])
    elif (data[2] == "non-anginal"):
        res.extend([0,0,1,0])
    else:
        res.extend([0,0,0,1])
    if (data[10] == "downsloping"):
        res.extend([1,0,0])
    elif (data[10] == "flat"):
        res.extend([0,1,0])
    else:
        res.extend([0,0,1])
    return res

def predict(data):
    res = proccess_data(data)
    df = pd.read_csv("train.csv")
    X_data = df.drop("num",axis = 1)
    Y_data = df["num"]
    model = RandomForestClassifier(max_depth = 5, max_features= 13, n_estimators = 150 )
    #model = RandomForestClassifier(max_depth = 6, max_features= 18, n_estimators = 50 )
    model.fit(X_data,Y_data)
    return (model.predict(np.reshape(res,(1,-1)))[0])