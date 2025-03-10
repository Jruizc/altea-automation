from selenium.webdriver import ActionChains
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from configuration.config import BaseConfig

class BasePage:

    def __init__(self, driver,logger):
        self.driver = driver
        self.logger=logger
        self.wait = WebDriverWait(driver, BaseConfig.IMPLICIT_WAIT)

    def click_element(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator)).click()
        except EX as e:
            self.logger.error("Exception No se puede hacer click en el elemento")

    def input_element(self, by_locator, text):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            self.logger.error("Exception El input no esta dispnible")

    def get_all_elements(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return self.driver.find_elements(*by_locator)
        except EX as e:
            self.logger.error("Exception No se encontraron los elementos en la web")

    def get_element(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator))
        except EX as e:
            self.logger.error("Exception No se encontro el elemento en la web")


    def wait_until_specific_element_is_not_displayed(self, by_locator):
        try:
            self.wait.until_not(EC.visibility_of_element_located(by_locator))
        except EX as e:
            self.logger.error("Exception El elemento está presente en pantalla")

    def scroll_into_view(self, by_locator):
        try:
            element=self.wait.until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except EX as e:
            self.logger.error("Exception El elemento no está presente en pantalla")

    def scroll_down(self, pixels):
        try:
            self.driver.execute_script("window.scrollBy(0, arguments[0]);",pixels)
        except EX as e:
            self.logger.error("Exception No se puede hacer scroll")
