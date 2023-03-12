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
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().PersonalDetails))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().FirstName))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().FirstName))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().FirstName))).send_keys(Data.Hrm_data().FirstName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().MiddleName))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().MiddleName))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().MiddleName))).send_keys(Data.Hrm_data().MiddleName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().lastName))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().lastName))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().lastName))).send_keys(Data.Hrm_data().lastName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().EmployeeId))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().EmployeeId))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().EmployeeId))).send_keys(Data.Hrm_data().EmployeeId)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId))).send_keys(Keys.CONTROL + "a")
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId))).send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().OtherId))).send_keys(Data.Hrm_data().OtherId)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Savebutton))).click()
        
OrangeHrm().login()