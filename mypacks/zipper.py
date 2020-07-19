import sys
import os
from os.path import basename

if sys.version_info >= (3, 8):
    import zipfile
else:
    import zipfile38

class Zipper:
    def __init__(self, paths=['./'], output='./sample.zip'):
        self.paths = paths
        self.output = output
        self.zip_obj = zipfile.ZipFile(self.output, 'w', zipfile.ZIP_DEFLATED)

    def is_dir(self, path):
        if os.path.isdir(path):
            return True
        return False

    def zip_single_file(self, file_path):
        self.zip_obj.write(file_path)

    def zip_directory(self, dir_path):
        for folder_name, subfolders, file_names in os.walk(dir_path):
            for file_name in file_names:
                if file_name != self.output.split('/')[-1]:
                    file_path = os.path.join(folder_name, file_name)
                    self.zip_obj.write(file_path)

    def finish(self):
        self.zip_obj.close()

    def zip(self):
        for path in self.paths:
            if self.is_dir(path):
                self.zip_directory(path)
            else:
                self.zip_single_file(path)

        self.finish()

        return self.output