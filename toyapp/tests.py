from django.test import TestCase

# Create your tests here.

# test 1

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        # Login
        submit1 = driver.find_element(By.ID, "login")
        submit1.click()
        time.sleep(2)


        username= driver.find_element(By.ID, "user")
        username.send_keys("linnujose")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("Rsjoi@10")
        
        submit1 = driver.find_element(By.ID, "sub")
        submit1.click()
        time.sleep(2)
        
        logout = driver.find_element(By.ID, "log")
        logout.click()
        time.sleep(2)


#test 2

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/login/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        

        username= driver.find_element(By.ID, "user")
        username.send_keys("linnujose")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("Rsjoi@10")
        
        submit1 = driver.find_element(By.ID, "sub")
        submit1.click()
        time.sleep(2)
        
        product = driver.find_element(By.ID, "pro")
        product.click()
        time.sleep(2)


#test 3

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/product_list/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

       
        
        submit1 = driver.find_element(By.ID, "wish")
        submit1.click()
        time.sleep(2)
        
        wish = driver.find_element(By.ID, "wish2")
        wish.click()
        time.sleep(2)




# main  project
# test 1
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        # Login
        submit1 = driver.find_element(By.ID, "login")
        submit1.click()
        time.sleep(2)


        username= driver.find_element(By.ID, "user")
        username.send_keys("Nandana")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("Nandana@123")
        
        submit1 = driver.find_element(By.ID, "sub")
        submit1.click()
        time.sleep(2)
        
        logout = driver.find_element(By.ID, "log")
        logout.click()
        time.sleep(2)




# test 2

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

       
        submit1 = driver.find_element(By.ID, "login")
        submit1.click()
        time.sleep(2)


        username= driver.find_element(By.ID, "user")
        username.send_keys("Nandana")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("Nandana@123")
        
        submit1 = driver.find_element(By.ID, "sub")
        submit1.click()
        time.sleep(2)
        
        wish = driver.find_element(By.ID, "wish")
        wish.click()
        time.sleep(2)


        wish2 = driver.find_element(By.ID, "wish22")
        wish2.click()
        time.sleep(2)



# test 3

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_complete_shopping_flow(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

       # Login
        submit1 = driver.find_element(By.ID, "login")
        submit1.click()
        time.sleep(2)


        username= driver.find_element(By.ID, "user")
        username.send_keys("admin")
        password = driver.find_element(By.ID, "pass")
        password.send_keys("Linnu@2001")
        
        submit1 = driver.find_element(By.ID, "sub")
        submit1.click()
        time.sleep(2)
        
        wish = driver.find_element(By.ID, "wish")
        wish.click()
        time.sleep(2)


        wish2 = driver.find_element(By.ID, "wish22")
        wish2.click()
        time.sleep(2)


        wish3 = driver.find_element(By.ID, "wish33")
        wish3.click()
        time.sleep(2)

        wish4 = driver.find_element(By.ID, "wish44")
        wish4.click()
        time.sleep(2)
