# Pornhub python utility
A python based utility tool to do various activities on your favourite website. No more manual, tiring work requiring hours to get your favourite content. Now everything at the click of a button.

## Setup
```
pip3 install -r requirements.txt
```

Make sure you also have your chromedriver executable in this folder.

## Run
```
python main.py <pornhub-channel-url>
```
This will fetch a list of every single video on the channel

### How to download single video
Open a python shell from the cloned directory
```
from downloaders.downloadmanager import DownloadManager

man = DownloadManager(save_path = "<path-to-save-folder>")
man.download(link = "<video-link>", quality = "720")
```

## Features
- get links of all videos from a channel page
- download videos directly from the link
- option to select video download quality
- support for concurrent file download to get faster download upto 8 times as that of a browser(if bandwidth is not a bottleneck)

## TODO
- Add multiple downloaders

