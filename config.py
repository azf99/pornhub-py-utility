import os
import platform

chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe") if platform.system() == "Windows" else os.path.join(os.getcwd(), "chromedriver")
default_page = "https://www.pornhub.org/pornstar/leana-lovings"
DEFAULT_VIDEO_LINK = "https://www.pornhub.org/view_video.php?viewkey=ph62e6e8b768ae2"
DEFAULT_QUALITY = "480"
DEFAULT_FILENAME = "download.mp4"
DOWNLOAD_CONNECTIONS = 8
