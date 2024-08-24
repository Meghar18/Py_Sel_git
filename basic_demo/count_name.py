from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
driver=WebDriver()
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
driver.find_element("name",'q').send_keys("megha")
sleep(1)
driver.find_element("name",'q').click()
elements=driver.find_elements("xpath",'//*[contains(text(),"megha")]')
sleep(1)
print(len(elements))
for ele in elements:
    print(ele.text)