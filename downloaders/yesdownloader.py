from selenium import webdriver
import pandas as pd
import time
import config

class YesDownloader(object):
    def __init__(self, quality = config.DEFAULT_QUALITY):
        self.URL = "https://yesdownloader.com/en1/"
        self.quality = quality

    def get_link(self):
        quality_matrix = pd.read_html(self.driver.find_element_by_xpath("//*[@id='dtable']").get_attribute('innerHTML'))[0]
        quality_matrix = quality_matrix.astype("string")
        index = quality_matrix[quality_matrix[0] == self.quality].index.values
        if len(index) == 0:
            print("Requested quality not found, downloading {}p instead".format(config.DEFAULT_QUALITY))
            indexdefault = quality_matrix[quality_matrix[0] == config.DEFAULT_QUALITY].index.values[0] + 1
            return self.driver.find_element_by_xpath("//*[@id='dtable']/table/tbody/tr[{}]/td[3]/a".format(indexdefault)).get_attribute("href")
        return self.driver.find_element_by_xpath("//*[@id='dtable']/table/tbody/tr[{}]/td[3]/a".format(index[0] + 1)).get_attribute("href")

    def get_filename(self):
        return self.filename

    def get_metadata(self, link):
        self.driver =  webdriver.Chrome(config.chromedriver_path)
        self.driver.get(self.URL)

        box = self.driver.find_element_by_id("ytUrl")
        box.send_keys(link)

        submitButton = self.driver.find_element_by_name("submitForm")
        submitButton.click()
        time.sleep(2)

        forwardlink = self.get_link()
        
        self.filename = self.driver.find_element_by_class_name("o2").text.strip() + ".mp4"

        self.driver.get(forwardlink)

        findtext = "Click here to start the download"

        self.driver.find_element_by_xpath("//*[contains(text(), 'Click here to start the download')]").click()
        time.sleep(10)

        downlink = self.driver.current_url
        self.driver.quit()

        return downlink, "_".join(self.filename.replace(":", "").split())