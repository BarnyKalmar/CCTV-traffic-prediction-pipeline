import os
from datetime import datetime as dt
import csv
from ultralytics import YOLO

custom_model= r"C:\CCTV_Proj\runs\detect\Final_Model\weights\best.pt"
model = YOLO(custom_model)

def count_cars(image_dir):

    ''''
    this function iterates over all cctv footage from a given month, extracts the pictures
    id,month,is_weekday,time of day, then feeds it to the fine-tuned yolo model to count the number of cars
    and appends these to a list of the unique picture which then gets appended to the monthly list
    '''

    #create the output directory for the month
    directory = os.listdir(image_dir)
    first_pic = directory[0]
    year_month = first_pic[10:16]
    output_dir = os.path.join(image_dir, f"{year_month}_traffic.csv")

    #extract relevant information
    with open(output_dir, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['id','month','day','time_of_day','is_weekday','car_count'])

        pic_count = 0

        for file in os.listdir(image_dir):
            if not file.endswith(('.jpg','.jpeg')):
                continue

            id = file[:9]
            date = file[10:18]
            month = file[14:16]
            day = file[16:18]
            time_of_day = file[19:23]

            str_date = str(date)
            converted_date = dt.strptime(str_date,"%Y%m%d")
            is_weekday = converted_date.weekday() <= 4

            image_path = os.path.join(image_dir,file)
            results = model(image_path,verbose=False)
            car_count = len(results[0].boxes)

            writer.writerow([id,month,day,time_of_day,is_weekday,car_count])
            pic_count += 1


            if pic_count % 500 == 0:
                print("stream flowing safely")

        print(f'processed {pic_count} pictures to {output_dir}')

