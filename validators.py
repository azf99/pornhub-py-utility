import sys
import requests
import urllib.parse as urlparse

class Validator(object):
    def __init__(self, url):
        self.url = url
        self.type = None

    def ph_type_check(self):
        parsed = urlparse.urlparse(self.url)
        self.type = parsed.path.split('/')[1]
        if self.type == "model":
            print("This is a MODEL url,")
        elif self.type == "pornstar":
            print("This is a PORNSTAR url,")
        elif self.type == "channels":
            print("This is a CHANNEL url,")
        elif self.type == "users":
            print("This is a USER url,")
        elif self.type == "playlist":
            self.type("This is a PLAYLIST url,")
        elif type == "view_video.php":
            print("This is a VIDEO url. Please paste a model/pornstar/user/channel/playlist url.")
            sys.exit()
        else:
            print("Somethings wrong with the url. Please check it out.")
            sys.exit()
        return self.type

    def ph_url_check(self):
        parsed = urlparse.urlparse(self.url)
        regions = ["www", "cn", "cz", "de", "es", "fr", "it", "nl", "jp", "pt", "pl", "rt"]
        for region in regions:
            if (parsed.netloc == region + ".pornhub.org") or (parsed.netloc == region + ".pornhub.com"):
                print("PornHub url validated.")
                return
        print("This is not a PornHub url.")
        sys.exit()

    def ph_alive_check(self):
        requested = requests.get(self.url)
        if requested.status_code == 200:
            print("and the URL is existing.")
        else:
            print("but the URL does not exist.")
            sys.exit()

    def run(self):
        self.type = self.ph_url_check()
        self.ph_type_check()
        self.ph_alive_check()
        return self.type

    def get_type(self):
        return self.type
