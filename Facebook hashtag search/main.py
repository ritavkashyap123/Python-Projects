#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

tag = input("Enter the hashtag = #")
n_scrolls = int(input("How much the page to be scrolled down : "))

#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/Tarali/chromedriver.exe', options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com/")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("xabcd989@gmail.com")
password.clear()
password.send_keys("Abcdxyz989@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click()

#We are logged in!

#To search hashtag
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search Facebook']")))
search.clear()
search.send_keys('#',tag)

#To enter hashtag page
for i in [tag]:
    driver.get('https://www.facebook.com/hashtag/'+tag+'/')
    time.sleep(5)
    
    #To done the scrolls
    for j in range(0,n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
    details = driver.find_elements_by_tag_name('span')
    details = [span.get_attribute('class') for span in details]
    print(details)
        



