import requests
import os

lat = 54.982791
lon = -1.611731
radius_m  = 10



def get_camera_ids(lat, lon, radius_m,):

    url = 'https://api.cctv.urbanobservatory.ac.uk/camera'

    call = requests.get(url, params = {'lat':lat, 'lon':lon, 'radius':radius_m})

    if call.status_code == 200:
        print(call.json())

    else:
        raise ('Error getting camera ids')


#cams = get_camera_ids(lat, lon, radius_m)
train_dates = ['202003','202004','202005','202006','202012']
test_dates = []

def get_archive_data(working_directory,dates):

    url = 'https://api.cctv.urbanobservatory.ac.uk/archive'

    for date in dates:
        call = requests.get(url, params = {'system_code':'NC_A167D2','yearmonth':date},stream=True)

        if not os.path.exists(working_directory):
            os.makedirs(working_directory)

        if call.status_code == 200:
            filename = f"traffic{date}.zip"
            file_path = os.path.join(working_directory, filename)

            #stream the zip files using 128kb batches to allow local use
            with open(file_path, 'wb') as f:
                for chunk in call.iter_content(chunk_size=131072):
                    f.write(chunk)
            print(f"zip saved as: {filename}")
        else:
            print(f"Error{call.status_code}")



