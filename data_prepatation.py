import os
import io
import numpy as np
from numpy.ma.core import append
from scipy.stats import kurtosis, skew
import csv


subject_folders = os.listdir("Sisfall_dataset")

new_csv = [[]]
for i in subject_folders:
    temp_folder = []
    temp_folder = os.listdir("Sisfall_dataset/" + i)
    number_files = len(temp_folder)
    for j in temp_folder:
        file = io.BytesIO(open("Sisfall_dataset/" + i + "/" + j, 'rb').read().replace(b';',b''))
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
        
        if (j[0] == "F"):
            line.append(1)
        else:
            line.append(0)
        

        new_csv.append(line)
        file.close()

with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(new_csv)

