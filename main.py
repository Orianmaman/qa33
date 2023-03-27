from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ----------positive log in----------
driver = webdriver.Chrome(r'C:\Users\97254\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
time.sleep(3)

username = driver.find_element(By.CSS_SELECTOR,'#user-name')
username.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys('secret_sauce')

sing_in = driver.find_element(By.CSS_SELECTOR,'#login-button')
sing_in.send_keys(Keys.ENTER)
time.sleep(3)

# ----------negative log in----------
driver = webdriver.Chrome(r'C:\Users\97254\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
time.sleep(3)
username = driver.find_element(By.CSS_SELECTOR,'#user-name')
username.send_keys('locked_out_user')

password = driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys('secret_sauce')

sing_in = driver.find_element(By.CSS_SELECTOR,'#login-button')
sing_in.send_keys(Keys.ENTER)
time.sleep(3)

# ----------sanity test----------
driver = webdriver.Chrome(r'C:\Users\97254\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
time.sleep(3)

#---------- full test confrium pay----------
driver = webdriver.Chrome(r'C:\Users\97254\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
time.sleep(3)

username = driver.find_element(By.CSS_SELECTOR,'#user-name')
username.send_keys('performance_glitch_user')

password = driver.find_element(By.CSS_SELECTOR,'#password')
password.send_keys('secret_sauce')

sing_in = driver.find_element(By.CSS_SELECTOR,'#login-button')
sing_in.send_keys(Keys.ENTER)
time.sleep(3)

add_cart = driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack')
add_cart.click()
time.sleep(3)

shopping_cart =  driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a')
shopping_cart.click()

checkout = driver.find_element(By.CSS_SELECTOR,'#checkout')
checkout.send_keys(Keys.ENTER)

first_name = driver.find_element(By.CSS_SELECTOR,'#first-name')
first_name.send_keys('orian')

last_name = driver.find_element(By.CSS_SELECTOR,'#last-name')
last_name.send_keys('maman')

zip_code = driver.find_element(By.CSS_SELECTOR,'#postal-code')
zip_code.send_keys('80151')

next = driver.find_element(By.CSS_SELECTOR,'#continue')
next.send_keys(Keys.ENTER)
time.sleep(3)

finish = driver.find_element(By.CSS_SELECTOR,'#finish')
finish.send_keys(Keys.ENTER)
time.sleep(3)