import joblib
import io
import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


'''
get file values, and prepare like data was prepared on data preparation, and send it to query to predict fall
'''
query = [[]]

file = io.BytesIO(open("InputTest/F14_SA02_R04.txt", 'rb').read().replace(b';',b''))
data = np.genfromtxt(file,dtype=int,delimiter=',')

line = []
for col in range(len(data.T)):
    min_ = min(data[:, col])
    max_ = max(data[:, col])
    mean_ = np.mean(data[:, col])
    variance = np.var(data[:, col])
    k = kurtosis(data[:, col])
    s = skew(data[:, col])
    
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

print(prediction)