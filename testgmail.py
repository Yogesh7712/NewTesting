from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from time import sleep

username=input("enter email id: ")
passwd =input("enter password: ")

url= "https://accounts.google.com/v3/signin/identifier?dsh=S-486154099%3A1678004825131789&authuser=0&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession"


driver = webdriver.Chrome('C:/Users/Admin/Downloads/chromedriver')

driver.get(url)
driver.maximize_window()

driver.find_element("id","identifierId").send_keys(username)
sleep(3)

driver.find_element("id","identifierNext").click()
sleep(3)

driver.find_element("name","Passwd").send_keys(passwd)
sleep(4)

driver.find_element("id","passwordNext").click()
sleep(4)

print("login successful")

driver.close









