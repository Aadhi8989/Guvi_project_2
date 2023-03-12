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
        #Pim        
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().pim))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().add_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().toggle_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().first_name))).send_keys(Data.Hrm_data().first_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().middle_name))).send_keys(Data.Hrm_data().meddle_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().last_name))).send_keys(Data.Hrm_data().last_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().user_name))).send_keys(Data.Hrm_data().username_pim)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().password))).send_keys(Data.Hrm_data().password_pim)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().password_con))).send_keys(Data.Hrm_data().con_password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().save_Button))).click()
        
          

OrangeHrm().login()