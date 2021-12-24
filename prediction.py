import joblib


'''
get file values, and prepare like data was prepared on data preparation, and send it to query to predict fall
'''

classifier = joblib.load('classifier.pkl')
prediction = classifier.predict(query)