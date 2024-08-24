from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
driver=WebDriver()
driver.get("file:///C:/Users/Megha%20R/Desktop/selenium/files/demo.html")
driver.maximize_window()
time.sleep(1)
# items=driver.find_elements('xpath','//select[@id="multiple_cars"]')
# for ele in items:
#     print(ele.text)

# elements=driver.find_elements('xpath','//input[@style="width: 202px;"]')
# items=["appkle","google",'facebook',"yahoo","yelp","flipkart","ehatsapp","instagram",'amazon','microsoft']
# for box,item in zip(elements,items):
#     box.send_keys(item)
#     time.sleep(1)

# clic=driver.find_elements('name','download')
# for ele in range(len(clic)-1,-1,-1):
#      clic[ele].click()
#      time.sleep(1)

# links=driver.find_elements('xpath','//a')
# for link in links:
#     link_text=link.text
#     url=link.get_attribute("href")
#     print(f"{link_text} : {url}")
#     time.sleep(1)

element=driver.find_element("id","multiple_cars")
s=Select(element)
cars=['Audi','BMW']
for car in cars:
    s.select_by_visible_text(car)
    time.sleep(1)
selected_item=s.all_selected_options
for item in selected_item:
    print(item.text)
s.deselect_all()