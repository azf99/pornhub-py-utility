from selenium import webdriver
import sys
import argparse

import config
from page import Page

# Create the parser
my_parser = argparse.ArgumentParser(description='Pornhub downloader utility')

# Add the arguments
my_parser.add_argument('-u',
                       '--url',
                       type=str,
                       help='the URL of the channel',
                       required = True)
my_parser.add_argument('-q',
                       '--quality',
                       type=str,
                       help='the video quality(240, 480, 720, etc.)',
                       default = config.DEFAULT_QUALITY)
my_parser.add_argument('-s',
                       '--save_path',
                       type=str,
                       help='the path to save the videos',
                       default = "default")

# Execute the parse_args() method
args = my_parser.parse_args()
# print(args.quality)
# URL = sys.argv[1] if len(sys.argv) > 1 else config.default_page
URL = args.url
driver = webdriver.Chrome(config.chromedriver_path)

pageNum = 0
maxPages = 100

page = Page(URL, driver, pageNum, maxPages, args.quality, args.save_path)

links = page.get_all_links()
print(links)
print("{} videos found".format(len(links)))
driver.quit()
page.download_videos()



# from downloaders.downloadmanager import DownloadManager

# man = DownloadManager(quality = "480")
# man.download(links[0])
