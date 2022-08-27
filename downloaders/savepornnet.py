from selenium import webdriver
import time
import config

class SavePornNet(object):
    def __init__(self):
        self.URL = "https://yesdownloader.com/en1/"
        self.driver =  webdriver.Chrome(config.chromedriver_path)

    def get_metadata(self, link):
        self.driver.get(self.URL)

        box = self.driver.find_element_by_id("ytUrl")
        box.send_keys(link)

        submitButton = self.driver.find_element_by_name("submitForm")
        submitButton.click()

        forwardlink = self.driver.find_elements_by_xpath("//*[@id='dtable']/table/tbody/tr[3]/td[3]/a")[0].get_attribute("href")
        filename = self.driver.find_element_by_class_name("o2").text.strip() + ".mp4"

        self.driver.get(forwardlink)

        findtext = "Click here to start the download"

        self.driver.find_element_by_xpath("//*[contains(text(), 'Click here to start the download')]").click()
        time.sleep(10)

        downlink = self.driver.current_url
        self.driver.quit()

        return downlink, filename