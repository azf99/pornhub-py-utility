# Pornhub python utility
A python based utility tool to do various activities on your favourite website. No more manual, tiring work requiring hours to get your favourite content. Now eveything at the click of a button.

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
man.download(link = "<video-link>")
```

## Features
- get links of all videos from a channel page
- download videos directly from the link

## TODO
- support for recognizing different link types(channels, playlists, etc.)
- Add multiple downloaders
- support for parallel file download
