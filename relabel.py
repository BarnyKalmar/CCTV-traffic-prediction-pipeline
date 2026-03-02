import os


def relabel(dataset,folders):

    for folder in folders:
        label = os.path.join(dataset,folder,'labels')

        if not os.path.exists(label):
            print(f'file {label} does not exist!')
            continue

        for file in os.listdir(label):
            if file.endswith('.txt'):
                path = os.path.join(label,file)

                with open(path,'r') as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) >0:
                        parts[0] = '0'
                        new_lines.append(' '.join(parts) + '\n')

                with open(path,'w') as f:
                    f.writelines(new_lines)
    print('successfully relabeled all files')


dataset = r'C:\CCTV_Proj\hand_labeled_data'
folders = ['training_set','validation_set','test_set']
relabel(dataset,folders)