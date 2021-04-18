import requests
import os
import pyprind
import sys
from multiprocessing.pool import ThreadPool as Pool



if len(sys.argv) < 2:
    print('Empty token for label_studio please visit label_studio documentation to learn how get you API token: https://labelstud.io/guide/api.html')
    sys.exit(-1)
else:
    label_studio_token = sys.argv[1]


def upload_file_to_label_studio(file_path):
    headers = {
        'Authorization': f"Token {label_studio_token}"
    }
    files = {
        'FileUpload': (file_path, open(file_path, 'rb')),
    }
    response = requests.post('http://localhost:8081/api/projects/1/import', headers=headers, files=files)


def worker(item):
    try:
        upload_file_to_label_studio(item)
    except:
        print(f"error with {item}")

pool = Pool()

for folder, subfolder, files in os.walk('/workspace/data'):
    if len(files) > 0:
        print(f"uploading folder : {folder}")
        for file in pyprind.prog_bar(files):
            file_path = os.path.join(folder, file)
            pool.apply_async(worker, (file_path,))

pool.close()
pool.join()
