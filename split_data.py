import os
import random
import shutil


source = r"C:\CCTV_Proj\labeled_filtered"
destination = r"C:\CCTV_Proj\hand_labeled_data"

jpegs = [im for im in os.listdir(source) if im.endswith('.jpg')]
random.shuffle(jpegs)

train_size = int(len(jpegs)*0.8)
validation_size = int(len(jpegs)*0.1)
test_size =  int(len(jpegs)*0.1)

training_files = jpegs[:train_size]
validation_files = jpegs[train_size:train_size+validation_size]
test_files = jpegs[train_size + validation_size:]


def migrate_files(files,split):

    image_dir = os.path.join(destination,split,'images')
    label_dir = os.path.join(destination,split,'labels')

    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

    for jpeg in files:
        label = jpeg.replace('.jpg','.txt')

        shutil.copy(os.path.join(source,jpeg),os.path.join(destination,split,'images',jpeg))

        if os.path.exists(os.path.join(source,label)):
            shutil.copy(os.path.join(source,label),os.path.join(destination,split,'labels',label))




migrate_files(training_files, 'training_set')
migrate_files(validation_files, 'validation_set')
migrate_files(test_files, 'test_set')

print(f" Successfully split data into '{destination}' folder.")

