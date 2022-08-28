import pandas as pd
import sys

from downloaders.downloadmanager import DownloadManager
from validators import Validator

class Page(object):
    def __init__(self, url, driver, pageNum, maxPages):
        self.URL = url
        self.driver = driver
        self.pageNum = pageNum
        self.maxPages = maxPages
        self.links = []
        self.type = Validator(self.URL).run()
        self.channel_name = self.URL.split("/")[-1].strip("/")

    def get_links_from_page(self):
        elems = self.driver.find_elements_by_xpath("//*[@class='videoUList clear-both']/ul/li/div/div/a")
        for elem in elems:
            href = elem.get_attribute("href")
            if "view_video.php?viewkey=" in href:
                self.links.append(href.split("&pkey")[0])
        return self.links

    def get_all_links(self):
        links = []
        while self.pageNum < self.maxPages:
            self.pageNum += 1
            self.driver.get("{}/videos?page={}".format(self.URL, self.pageNum))
            
            print(self.driver.title)
            if self.driver.title == "Page Not Found":
                print("Stopping")
                break
            self.get_links_from_page()
        df = pd.Series(self.links)
        self.links = df.drop_duplicates().tolist()
        print("{} videos found".format(len(self.links)))

        out_text = "\n".join(self.links)

        with open(self.channel_name + "-links.txt", "w") as outfile:
            outfile.write(out_text)
        return self.links

    def download_videos(self):
        man = DownloadManager(quality = "480")

        for link in self.links:
            man.download(link)