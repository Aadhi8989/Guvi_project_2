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
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Salary_BUTTON))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Salary_ADD))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Deposit_toggle))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().SalaryComponent))).send_keys(Data.Hrm_data().SalaryComponent)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().PayGrade))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().PayGrade_select))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().PayFrequency))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().PayFrequency_sel))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Currency))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Currency_select))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Amount))).send_keys(Data.Hrm_data().Amount) 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().AccountNumber))).send_keys(Data.Hrm_data().AccountNumber)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().AccountType))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().AccountType_select))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().RoutingNumber))).send_keys(Data.Hrm_data().RoutingNumber)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Amount_2))).send_keys(Data.Hrm_data().Amount_2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Hrm_locators().Savebutton))).click() 

     

OrangeHrm().login()