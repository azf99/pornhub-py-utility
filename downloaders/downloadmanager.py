import urllib.request
import os
import sys
import time
import shutil
import threading
import requests
from tqdm import tqdm
from urllib.parse import urlparse


from .yesdownloader import YesDownloader
# from progressbars.ProgressBar import show_progress
import config

class DownloadManager(object):
    def __init__(self, quality = config.DEFAULT_QUALITY, save_path = "./", choice = "yesdown"):
        self.save_path = save_path
        self.conns = config.DOWNLOAD_CONNECTIONS
        self.tmp_dir = './tmp/'
        if not os.path.isdir(self.tmp_dir):
            os.mkdir(self.tmp_dir)
        self.dl_dir = save_path
        if not os.path.isdir(self.dl_dir):
            os.mkdir(self.dl_dir)
        
        if choice == "yesdown":
            self.downloader = YesDownloader(quality = quality)

    def download_chunk(self, url, start, this_chunk_size, part):
        r = requests.get(url, headers={'Range':'bytes=%d-%d' % (start, start + this_chunk_size-1)}, stream=True)
        filename = self.filename + '_%d' % part
        filepath = os.path.join(self.tmp_dir, filename)
        #print('Downloading %s' % filepath)
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        #print ('Downloaded %s' % filepath)

    def download(self, link = config.DEFAULT_VIDEO_LINK):
        url, self.filename = self.downloader.get_metadata(link)
        print(url, self.filename)

        # check if URL accept ranges
        r = requests.head(url)
        accept_ranges = 'accept-ranges' in r.headers and 'bytes' in r.headers['accept-ranges']
        if not accept_ranges:
            print('URL does not accept byte ranges.')
            quit()

        # download chunks
        size = int(r.headers['content-length'])
        chunk_size = (size // self.conns)
        remainder = (size % self.conns)
        threads = []
        for start in range(0, size, chunk_size):
            part = len(threads)
            this_chunk_size = chunk_size if part != self.conns-1 else chunk_size + remainder
            t = threading.Thread(target=self.download_chunk, args=(url, start, this_chunk_size, part))
            threads.append(t)
            t.daemon = True
            t.start()

        for thread in tqdm(threads):
            thread.join()

        print('All parts downloaded. Joining files...')

        # stitching the chunks into single file
        filepath = os.path.join(self.dl_dir, self.filename)
        with open(filepath, 'wb') as f:
            for i in range(self.conns):
                tmp_filename = self.filename + '_%d' % i
                tmp_filepath = os.path.join(self.tmp_dir, tmp_filename)
                shutil.copyfileobj(open(tmp_filepath, 'rb'), f)
                os.remove(tmp_filepath)

        print('Joining complete. File saved in %s' % filepath)