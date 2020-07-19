from .uploader import Uploader

class UploaderBuilder:

    paths = ''
    output = './sample.zip'
    zipping_mode = False
    parent_id = ''
    interval = 60

    def set_path(self, paths):
        self.paths = paths
        return self

    def set_output(self, output):
        self.output = output
        return self

    def set_zipping_mode(self, status):
        self.zipping_mode = status
        return self

    def set_parent_id(self, parent_id):
        self.parent_id = parent_id
        return self

    def set_interval(self, interval):
        self.interval = interval
        return self

    def build(self):
        return Uploader(
            self.paths,
            self.output,
            self.zipping_mode,
            self.parent_id,
            self.interval)
            