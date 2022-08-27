from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

import config
from page import Page

URL = sys.argv[1] if len(sys.argv) > 1 else config.default_page

driver = webdriver.Chrome(config.chromedriver_path)

pageNum = 0
maxPages = 2

page = Page(URL, driver, pageNum, maxPages)

links = page.get_all_links()
print(links)
print("{} videos found".format(len(links)))

driver.quit()

from downloaders.downloadmanager import DownloadManager

man = DownloadManager()
man.download(links[0])
