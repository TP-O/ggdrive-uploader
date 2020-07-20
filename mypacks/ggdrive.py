import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GGDrive:

    def __init__(self, parent_id):
        self.parent_id = parent_id

    def start(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.ggdrive = GoogleDrive(gauth)
        return self

    def get_file_list(self):
        return self.ggdrive.ListFile({
            'q': "'%s' in parents and trashed=false" % self.parent_id
        }).GetList()

    def update(self, file_item, path):
        file_item.SetContentFile(path)
        file_item.Upload()
        subprocess.Popen(['notify-send', 'Item was updated!'])

    def upload(self, paths):
        file_list = self.get_file_list()
        for path in paths:
            is_exist = False
            title = path.split('/')[-1]
            for file_item in file_list:
                if file_item['title'] == title:
                    self.update(file_item, path)
                    is_exist = True
                    break
            if not is_exist:
                file_item = self.ggdrive.CreateFile({'title': title, 'parents': [{'id': self.parent_id}]})
                file_item.SetContentFile(path)
                file_item.Upload()
                subprocess.Popen(['notify-send', 'Item was uploaded!'])