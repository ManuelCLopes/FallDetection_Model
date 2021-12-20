import os
import io
import numpy as np

subject_folders = os.listdir("Sisfall_dataset")
for i in subject_folders:
    temp_folder = []
    temp_folder = os.listdir("Sisfall_dataset/" + i)
    number_files = len(temp_folder)
    #print("\n" + i + ":" + str(number_files))

    final_list = [] 
    for j in temp_folder:
        #print("\t" + j)
        if(j == "F15_SA21_R02.txt"):
            s = io.BytesIO(open("Sisfall_dataset/" + i + "/" + j, 'rb').read().replace(b';',b''))
            data = np.genfromtxt(s,dtype=int,delimiter=',')
            print("Max amplitude: " + str(max(data[:, 0])))
            print("Min amplitude: " + str(min(data[:, 0])))
            print("Mean amplitude: " + str(np.mean(data[:, 0])))
            print("Variance: " + str(np.var(data[:, 0])))
            print("Kurtosis: " + str(kurtosis(data[:, 0])))
            print("Skewness: " + str(np.mean(data[:, 0])))

