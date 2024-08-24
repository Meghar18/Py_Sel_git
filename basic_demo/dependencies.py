from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from re import findall
from selenium.webdriver.support.select import Select
driver=WebDriver()
# driver.get("file:///C:/Users/Megha%20R/Desktop/selenium/files/demo.html")
# sleep(1)
# driver.find_element("xpath",'//td[text()="Python"]/..//input[@name="download"]').click()
# sleep(1)
# cars=driver.find_element("xpath",'//select[@id="multiple_cars"]')
# sleep(1)
# s=Select(cars)
# items=s.options
# _items=[item.text for item in items]
# for item in _items:
#     s.select_by_visible_text(item)
#     sleep(1)
# s.deselect_all()
#------------------------------------------------------------------
# driver.get("https://www.shoppersstack.com/sub-category/women-ethnic-wear")
# sleep(1)
# driver.find_element("xpath","//span[text()='lavie']/../..//button[@type='button']").click()
# sleep(1)
# driver.get("https://www.python.org/downloads/")
# sleep(1)
# driver.find_element("xpath","//a[text()='Python 3.10.14']/../..//a[text()='Release Notes']").click()
# sleep(1)
# driver.get("https://demowebshop.tricentis.com/books")
# element=driver.find_elements("xpath",'//span[@class="price actual-price"]')
# # for ele in element:
# #     print(ele.text)
#____________________________________
#price comparision
# books=["Computing and Internet","Fiction","Health Book"]
# for book in books:
#     _xpath=f"//a[text()='{book}']/../..//span[@class='price actual-price']"
#     price=driver.find_element("xpath",_xpath).text
#     print(f"Price of {book} is {price} ")
#     sleep(1)
# dict={"Computing and Internet":11.00,"Fiction":24.00,"Health Book":10.00}
# for item,price in dict.items():
#     __xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     __price=driver.find_element("xpath",__xpath).text
#     if price==float(__price):
#         print(f"price of {item} is matching with {price}")
#     else:
#         print(f"price of {item} is not matching with {price}")
#--------------------------------------------------------
#Adding a particular book to cart

# driver.get("https://demowebshop.tricentis.com/books")
# books=["Computing and Internet","Fiction","Health Book"]
# for book in books:
#     cart=driver.find_element('xpath',f"//a[text()='{book}']/../..//input[@type='button']")
#     cart.click()
#     sleep(1)
#
# driver.find_element('link text','Shopping cart').click()
# sleep(5)
# driver.find_element('xpath',"(//a[text()='Health Book'])[2]/../..//input[@type='checkbox']").click()
# sleep(2)
# driver.find_element('name','updatecart').click()
# sleep(2)

#-----------------------------------------------------
#Sauce demo costliest and least cost product

# driver.get("https://www.saucedemo.com/")
# sleep(1)
# driver.maximize_window()
# sleep(1)
# driver.find_element("id","user-name").send_keys("standard_user")
# sleep(1)
# driver.find_element("id",'password').send_keys("secret_sauce")
# sleep(1)
# driver.find_element("id","login-button").click()
# sleep(1)
#
# items=driver.find_elements("xpath","//div[@class='inventory_item_name ']")
# new_item=[]
# for item in items:
#     new_item.append(item.text)
#
# prices=driver.find_elements("class name","inventory_item_price")
# new_price=[]
# for price in prices:
#         exact_price=float("".join(findall(r"[\d\.]+",price.text)))
#         new_price.append(exact_price)
# dict_item={item:cost for item,cost in zip(new_item,new_price)}
# sort_item=sorted(dict_item.items(), key=lambda value: value[-1])
# max=sort_item[-1]
# min=sort_item[0]
# print(dict_item)
# print(sort_item)
# print(max)
# print(min)


