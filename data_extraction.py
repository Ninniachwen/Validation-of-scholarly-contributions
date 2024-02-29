# data extraction

#1. download the [trial-data](https://github.com/ncg-task/trial-data)
# 2. 

import os
import shutil


postfix = ".pdf" #"-Grobid-out.txt"
folder = "trial-data"
new_folder = "original_data" #"grobit"
base_path = os.getcwd()
path = os.path.join(base_path, folder)

if new_folder not in os.listdir(path):
    os.mkdir(os.path.join(path, new_folder))
    print("created new folder", new_folder)

for task_folder in os.listdir(path):
    task_folder_path = os.path.join(path, task_folder)
    if os.path.isdir(task_folder_path) & ("." not in task_folder):
        for paper_folder in os.listdir(task_folder_path):
            paper_folder_path = os.path.join(path, task_folder, paper_folder)
            if os.path.isdir(paper_folder_path):
                for filename in os.listdir(paper_folder_path):
                    if filename.endswith(postfix):
                        new_filename = f"{task_folder[0]}_{paper_folder}_{filename}"
                        source = os.path.join(paper_folder_path, filename)
                        destination = os.path.join(path, new_folder, new_filename)
                        print(f'copy from: {source}\n       to: {destination}')
                        shutil.copyfile(source, destination)