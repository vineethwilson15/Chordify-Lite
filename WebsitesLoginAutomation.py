from selenium import webdriver
import yaml

conf = yaml.load(open('loginDetails.yml'))
myChEmail = conf['chordify_user']['email']
myChPassword = conf['chordify_user']['password']

driver = webdriver.Chrome()

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_name(usernameId).send_keys(username)
   driver.find_element_by_name(passwordId).send_keys(password)
   driver.find_element_by_css_selector(submit_buttonId).click()

login("https://chordify.net/user/signin", "email", myChEmail, "password", myChPassword, 
         "#login > main > div > form > div.b1ix7qfq > button.s1pq8kw9.c1st8crj.b136ilgh")
