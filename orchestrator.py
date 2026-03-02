import os
from zipfile import ZipFile
import pyspark as spark
from API_get_archive import get_archive_data
from count_cars import count_cars
from regression_learner import deploy_schema



work_directory = r'C\CCTV_Proj'
train_dates = ['202003','202004','202005','202006','202007','202008']



def deploy_pipeline(work_directory,train_dates):

    #get all zip files from the API
    for date in train_dates:
        print(f'processing data for month: {date} ')
        get_archive_data(work_directory,date)

        #unzip each month's data
        zip_path = os.path.join(work_directory,f"traffic{date}.zip")
        extract_directory = os.path.join(work_directory, date)

        if os.path.exists(zip_path):
            print(f"unzipping file for month: {date} ")
            with ZipFile(zip_path,'r') as zip_file:
                zip_file.extractall(extract_directory)

            #feed the data to the YOLO model
            print(f'running YOLO model for month: {date} ')
            count_cars(extract_directory)

            #delete processed data
            for file in os.listdir(extract_directory):
                if file.endswith(('.jpg','.jpeg')):
                    os.remove(os.path.join(extract_directory,file))

        else:
            print(f'data for month: {date} is unavailable')

        csv_path = f"{work_directory}/*/*.csv"
        print('initiating Pyspark regression learner')

        deploy_schema(csv_path)

        print('pipeline ran successfully')



    if __name__ == '__main__':
        deploy_pipeline(work_directory,train_dates)















