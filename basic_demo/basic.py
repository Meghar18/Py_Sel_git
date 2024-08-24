# from selenium.webdriver.chrome.webdriver import WebDriver
# from time import sleep
# driver=WebDriver()
# driver.get("www.google.com")
# sleep(1)
# driver.find_element('id','input').send_keys("Megha")
# sleep(1)
# driver.maximize_window()
#
# sleep(1)
# driver.close()

from selenium import webdriver
import time
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver. Chrome(options=opts)

# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element('css selector',"a[class='ico-register']").click()
# driver.find_element('xpath',"(//input[@type='radio'])[2]").click()
# driver.find_element('css selector',"input[id='FirstName']").send_keys("Hello")
# driver.find_element('xpath','(//input[@class="text-box single-line"])[2]').send_keys("world")
# driver.find_element('xpath','(//input[@id="Email"])').send_keys("abc@gfmail.com")
# driver.find_element('xpath','//input[@name="Password"]').send_keys("abc@123")
# driver.find_element('css selector','input[name="ConfirmPassword"]').send_keys("abc@123")
# driver.find_element('id',"register-button").click()
# driver.find_element('partial link text','Apparel').click()

driver.get('https://www.myntra.com/')
driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys("Adidas Shoes")
driver.find_element('xpath',"//a[@class='desktop-submit']").click()
shoe_name=driver.find_elements('xpath','//h4[@class="product-product"]')
shoe_price=driver.find_elements('xpath','//div[@class="product-price"]')
for name, price in zip(shoe_name,shoe_price):
    print(name.text," = ",price.text)