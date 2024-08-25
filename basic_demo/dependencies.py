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
#----------------------------price comparision
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
#---------------------------Sauce demo costliest and least cost product

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
#-----------------------------------------------------
#--------------------------------demoweb shop jewellery cost nd its name ------------------
# driver.get("https://demowebshop.tricentis.com/jewelry")
# driver.maximize_window()
# products=driver.find_elements('xpath','//h2[@class="product-title"]')
# prod=[]
# for product in products:
#     prod.append(product.text)
#     sleep(1)
# print(prod)
# prices=driver.find_elements('xpath','//span[@class="price actual-price"]')
# priz=[]
# for price in prices:
#     priz.append(price.text)
#     sleep(1)
# print(priz)
# actual_cost=[]
# for ele in priz:
#     print(ele)
#     actual=float("".join(findall(r"[\d\.]",ele)))
#     actual_cost.append(actual)
# print(actual_cost)
# prod_cost={item:cost for item,cost in zip(prod,actual_cost)}
# print(prod_cost)
# sort_price=sorted(prod_cost.items(), key=lambda items:items[-1])
# print(sort_price[-1])
# print(sort_price[0])
#--------------------------------------------
#----------------------------------Apple phon ename and value compare fetching highest nd lowest cost
# driver.get("https://www.amazon.in/s?k=iphone&crid=3NGQB6WG05N00&sprefix=iphon%2Caps%2C271&ref=nb_sb_noss_2")
# driver.maximize_window()
# products=driver.find_elements('xpath','//span[@class="a-size-medium a-color-base a-text-normal"]')
# items=[]
# for product in products:
#     items.append(product.text)
#     sleep(1)
# print(items)
# costs=driver.find_elements('xpath','//span[@class="a-price-whole"]')
# cost=[]
# for prize in costs:
#     cost.append(prize.text)
#     sleep(1)
# print(cost)
# new_cost=[float(ele.replace(",","")) for ele in cost]
# print(new_cost)
# prod_cost_dict={prod:value for prod,value in zip(items,new_cost)}
# print(prod_cost_dict)
# prod_sort=sorted(prod_cost_dict.items(),key=lambda prod_item:prod_item[-1])
# print(prod_sort)
# print(prod_sort[-1])
# print(prod_sort[0])
#----------------------------------------------------
#Flipkart price and value max and min

# driver.get("https://www.flipkart.com/gaming-accesories/controllers/gamepads/pr?sid=4rr,km5,dom,a7g&fm=neo%2Fmerchandising&iid=M_59b9b1c3-9d20-4585-ae50-b9795a956e97_1_372UD5BXDFYS_MC.RITRJDS8NN9O&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Electronics~Gaming~Gamepads_RITRJDS8NN9O&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L2_view-all&cid=RITRJDS8NN9O")
# driver.maximize_window()
# sleep(1)
# item_names=driver.find_elements('xpath','//a[@class="wjcEIp"]')
# list_items=[]
# for item_name in item_names:
#     list_items.append(item_name.text)
# sleep(1)
# print(list_items)
# item_costs=driver.find_elements('xpath','//div[@class="Nx9bqj"]')
# list_costs=[]
# for item_cost in item_costs:
#     list_costs.append(item_cost.text)
# sleep(1)
# print(list_costs)
# new_list=[]
# for ele in list_costs:
#     new_list.append(int("".join(findall(r'[\d]',ele))))
# print(new_list)
# item_cost_dict={prod:price for prod,price in zip(list_items,new_list)}
# print(item_cost_dict)
# sort_dict=sorted(item_cost_dict.items(), key=lambda product:product[-1])
# print(sort_dict)
