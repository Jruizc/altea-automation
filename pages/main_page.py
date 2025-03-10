from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    INPUT_JOB_NAME = (By.NAME, "job_search")
    NAME_LIST_OFFERS = (By.CSS_SELECTOR,".wp-block-jobboard-loop a b")
    JOBS_COUNT = (By.CSS_SELECTOR,"[class*=filter__counts] > span:first-child")
    CATEGORY_LIST = (By.CSS_SELECTOR,".accordion-item")

    def __init__(self, driver,logger):
        super().__init__(driver,logger)

    def search_job_by_name(self,nombre):
        self.input_element(self.INPUT_JOB_NAME,nombre+Keys.RETURN)

    def get_list_offers_names(self):
        return self.get_all_elements(self.NAME_LIST_OFFERS)


    def get_offers_number(self):
        self.wait_until_specific_element_is_not_displayed(self.CATEGORY_LIST)
        n=self.get_element(self.JOBS_COUNT).text.replace(" ", "")
        return int(n)
