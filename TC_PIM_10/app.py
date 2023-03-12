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
        #Page1       
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, Locators.Hrm_locators().pim))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().edit_button))).click()
        #pag2
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().job_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Termination))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().TerminationDate))).send_keys(Data.Hrm_data().TerminationDate)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().TerminationReason))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Data.Hrm_data().TerminationReason))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Note))).send_keys(Data.Hrm_data().Note)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().savebutton))).click()


          

OrangeHrm().login()