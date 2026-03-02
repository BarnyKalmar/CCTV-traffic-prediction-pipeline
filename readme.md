# Yolo traffic prediction pipeline 


# Data engineering and ML pipeline that uses image classification and time series analysis to predict traffic flow for Newcastle upon Tyne highway camera footage


# This project implements  a pipeline for the Newcastle upon Tyne highway camera footage. The pipeline pulls zip files from the uk's ubranobservatory.ac API, then unzips the files and extracts relevant information from the cctv pictures such as time of day, day of week, number of cars. The project uses a finetuned version of YOLO-m to recognize car's which was trained on a set of hand labelled images from the cctv footages. The extracted informations are then output to a single csv file for all pictures of the given month, which is then fed to the the pyspark module, where it gets converted into a spark vector set and is the training set for the pyspark random forest regressor to better understand the dynamics and patters of the Newcastle upon Tyne traffic network.




#tech stack 
 -python
 -YOLO
 -LabelImg
 -Pyspark
 

# Scripts 
- API_get_archive.py : this script searches for available cameras based of input coordinates then pulls the zip files from the API for the specified timeframe 
- relabel.py : this function relabels the .txt files containing the hand labelled locations of cars to 0 instead of 4(default for cars in LabelImg) to 0 to make it YOLO compatible
- split_data.py: this function splits the handlabeled image folder into training,testing and validation sets using a randomized split 
- count_cars.py: this script extracts relevant information from the jpeg cctv pictures such as : time of day, month, is_weekday. Then feeds the picture to the finetuned Yolo model to count the number of cars which are then also added to the output csv 
- regression_learner.py: this script assembles the vector dataframe from the traffic.csv for Pyspark RandomForestRegression ingestion, then trains and tests the model to predict the number of cars based on time series analysis 
- orchestrator.py: this script automates the whole pipeline and runs it using if __name__ == '__main__':
 




