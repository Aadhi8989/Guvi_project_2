from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data
from Test_Locators import Locators
from time import sleep

#TestCase_PIM_01

class OrangeHrm:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    def __init__(self):
        self.driver.get(Data.Hrm_data().url)

    def login(self):
        #Login_Page
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Hrm_locators().username_Box))).send_keys(Data.Hrm_data().username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.Hrm_locators().password_Box))).send_keys(Data.Hrm_data().password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().login_botton))).click()
        #s
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_1)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_2)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_3)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_4)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_5)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_6)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_7)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_8)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_9)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_10)
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().search_Box))).send_keys(Data.Hrm_data().text_11)
          

OrangeHrm().login()