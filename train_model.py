import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score  

from sklearn.svm import SVC

import joblib
  
dataframe = pd.read_csv('test.csv')

descriptive = dataframe.iloc[:, :54].values
target = dataframe.iloc[:, 54].values

encoder = LabelEncoder()
n_cols = len(descriptive.T)
for i in range(n_cols):
    descriptive[:,i] = encoder.fit_transform(descriptive[:,i])


descriptive_train, descriptive_test, target_train, target_test = train_test_split(descriptive, target, test_size = 0.20, random_state = 0, )


standard_scaler = StandardScaler()
descriptive_train[:,:] = standard_scaler.fit_transform(descriptive_train[:,:]) #calcula e aplica
descriptive_test[:,:] = standard_scaler.transform(descriptive_test[:,:]) #aplica

classifier = SVC()
classifier.fit(descriptive_train, target_train)
prediction = classifier.predict(descriptive_test)


joblib.dump(classifier, 'classifier.pkl')

accuracy = accuracy_score(target_test, prediction)
print("\nAccuracy: " + str(accuracy))
matrix = confusion_matrix(target_test, prediction)
print("\nMatrix:\n" + str(matrix)) 