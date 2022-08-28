import urllib.request
import os

from .savepornnet import SavePornNet
from progressbars.ProgressBar import show_progress
import config

class DownloadManager(object):
    def __init__(self, quality = config.DEFAULT_QUALITY, save_path = "./", choice = "saveporn"):
        self.save_path = save_path
        if choice == "saveporn":
            self.downloader = SavePornNet(quality = quality)
    
    def download(self, link = "https://www.pornhub.org/view_video.php?viewkey=ph62e6e8b768ae2"):
        downlink, filename = self.downloader.get_metadata(link)
        print(downlink, filename)
        urllib.request.urlretrieve(downlink, os.path.join(self.save_path, filename), show_progress)
        print("{} downloaded successfully".format(filename))

