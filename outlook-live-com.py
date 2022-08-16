import selenium
from selenium import webdriver
import time

print("""
                        Hello Friends I'am Esen
                        outlook.live.com automatic program for login
                            | |
                            \\ /



""")

give_mail = input(str("Hotmail: "))
give_password = input(str("Password: "))

browser = webdriver.Chrome()
time.sleep(1)
url = "https://outlook.live.com/owa/"
browser.get(url)
browser.maximize_window()
time.sleep(1)
login = browser.find_element("xpath","/html/body/header/div/aside/div/nav/ul/li[2]/a")
login.click()
time.sleep(1)
mail = browser.find_element("xpath","/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
mail.send_keys(give_mail)
mail_next_button = browser.find_element("xpath","/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")
mail_next_button.click()
time.sleep(2)
password = browser.find_element("xpath","//*[@id='i0118']")
password.send_keys(give_password)
time.sleep(1)
password_button = browser.find_element("id","idSIButton9")
password_button.click()
time.sleep(1)
no = browser.find_element("id","idBtn_Back")
no.click()

 




