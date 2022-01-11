import joblib
import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def fall_detection(dados):
    data = pd.read_csv(dados, header=None)
    query = [[]]
    line = []
    for col in range(len(data.T)):
        min_ = min(data.iloc[:, col])
        max_ = max(data.iloc[:, col])
        mean_ = np.mean(data.iloc[:, col])
        variance = np.var(data.iloc[:, col])
        k = kurtosis(data.iloc[:, col])
        s = skew(data.iloc[:, col])
        
        line.append(min_)
        line.append(max_)
        line.append(mean_)
        line.append(variance)
        line.append(k)
        line.append(s)


    query[0] = line

    test = pd.DataFrame(query[0])
    descriptive = test.iloc[:, :54].values

    encoder = LabelEncoder()
    n_cols = len(descriptive.T)
    for i in range(n_cols):
        descriptive[:,i] = encoder.fit_transform(descriptive[:,i])


    standard_scaler = StandardScaler()
    descriptive = standard_scaler.fit_transform(descriptive)

    descriptive = descriptive.transpose()



    classifier = joblib.load('classifier.pkl')
    prediction = classifier.predict(descriptive)

    if prediction[0] == 1:
        return True
    else:
        return False