from .ggdrive import GGDrive
from .zipper import Zipper
from time import sleep
import os

class Uploader:
    def __init__(self, paths, output, zipping_mode, parent_id, interval):
        self.paths = paths
        self.output = output
        self.zipping_mode = zipping_mode
        self.parent_id = parent_id
        self.interval = interval

    def zip(self):
        if self.zipping_mode:
            zipper = Zipper(self.paths, self.output)
            return [zipper.zip()]
        for path in self.paths:
            if os.path.isdir(path):
                raise Exception('Zipping mode must be turned on!')
        return self.paths

    def upload(self):
        while True:
            sleep(self.interval)
            drive = (GGDrive(self.parent_id)
                    .start()
                    .upload(self.zip()))