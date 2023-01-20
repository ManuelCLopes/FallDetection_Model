# FallDetection_Model
Fall Detection Model using Sisfall dataset and SVC algorithm

Model used in project "An Intelligent and Scalable IoT Monitoring Framework for Safety in Civil Construction Workspaces" [1]

"
The ML model was trained from the Sisfall dataset. This dataset contains falls and activities of daily living (ADLs) acquired with a self-developed device composed of two types of accelerometer and one gyroscope. It consists of 19 activities of daily living (ADLs) and 15 fall types performed by 23 young adults, 15 ADL types performed by 14 healthy and independent participants over 62 years old, and data from one participant of 60 years old that performed all ADLs and falls. This dataset includes 4,510 files, each one of them corresponding either to falls or activities. Their content includes information regarding 3 tri-axial sensors: 2 accelerometers and 1 gyroscope with a frequency of 200 Hz. Moreover, includes gender and age. This information was used to take into account the activity files of the people who most fit the profile of construction workers (majority of male adults), to get closer to better-adapted predictions, and consequently less fallible, to most people who will make use of the system.

The files were processed to make convert them into records with the features containing information about their specific target (fall or activity). 6 different features were extracted distinguishing the type of fall from activities: the minimum, maximum, average, variation, kurtosis, and the skewness of the data of each sensor. Therefore, an initial set of files with 9 features ( accelerometer1(x,y,z) + accelerometer2(x,y,z) + gyroscope(x,y,z)) was converted to a dataset containing 54 features (9x6). After having a dataset with 54 features and the target, a standardization was made to process all values to an approximate scale, reducing possible prediction errors.

The implementation of the ML model was supported by the Support Vector Classification (SVC) algorithm. This model predicts two classes: fall and activity.
"

References:

[1] Ferreira, C., Correia, L., Lopes, M., Henriques, J., Martins, P., Wanzeller, C., & Caldeira, F. (2023). An Intelligent and Scalable IoT Monitoring Framework for Safety in Civil Construction Workspaces. In J. F. and L. R. A. J. de la Iglesia Daniel H. and de Paz Santana (Ed.), New Trends in Disruptive Technologies, Tech Ethics and Artificial Intelligence (pp. 69–78). Springer International Publishing.
