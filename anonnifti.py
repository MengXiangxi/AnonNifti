import configparser
import subprocess
import csv
import os

def create_folder(folder_name):
    if os.path.exists(folder_name):
        raise Exception(f"Folder '{folder_name}' already exists.")
    else:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")

config = configparser.ConfigParser()
config.read('./CONFIG')
dcm2niix_path = config['DEFAULT']['dcm2niix_path']
input_dir = config['DEFAULT']['input_dir']
output_dir = config['DEFAULT']['output_dir']
list_path = config['DEFAULT']['list_path']

if os.path.exists('error_log.txt'):
    os.remove('error_log.txt')

with open(list_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        real_name = row['RealName']
        anon_name = row['AnonName']
        study_in = os.path.join(input_dir, real_name)
        nifti_out = os.path.join(output_dir, anon_name)
        try:
            create_folder(nifti_out)
        except Exception as e:
            print(str(e))
            with open('error_log.txt', 'a') as error_log:
                error_log.write(str(e) + '\n')
            continue
        command = dcm2niix_path + ' -b n -z y' + ' -o ' + nifti_out + ' -f %d ' + study_in
        subprocess.run(command)