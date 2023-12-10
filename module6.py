import shutil
import os

data_residence = {'Michel':'Canada', 'John':'USA', 'Liza':'Australia'}

def create_backup(path, file_name, employee_residence):
    with open(fr'{path}\{file_name}', 'wb') as f:

        for key, value in employee_residence.items():
            line = f'{key} {value}\n'.encode()
            f.write(line)

        archive = shutil.make_archive('backup_folder', 'zip', path)
        result = os.getcwd()
        return result

print(create_backup('GO_IT_RHA', 'output.txt.', data_residence))
