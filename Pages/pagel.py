

class Log():

    def __init__(self,driver):
        self.driver = driver

        self.search_id = "//*[@title='Search']"
        self.searchbtn = "//*[@value='Google Search']"

    def entersearch(self,search):
        self.driver.find_element_by_xpath(self.search_id).send_keys(search)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.searchbtn).click()