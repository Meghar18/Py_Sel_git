import  time
from selenium import  webdriver
from selenium.webdriver.support.select import Select
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/Megha%20R/Desktop/selenium/files/demo.html")
sel_car=driver.find_element('xpath','//select[@id="standard_cars"]')
s=Select(sel_car)
s.select_by_visible_text('Audi')
time.sleep(1)
s.select_by_value('hda')
time.sleep(1)
s.select_by_index(5)
time.sleep(1)
print(s.first_selected_option.text)
sel_item=driver.find_elements('xpath','//select[@id="multiple_cars"]')

for ele in sel_item:
    s1=Select(ele)
    s1.select_by_value('hda')
    s1.select_by_index(4)
    s1.select_by_visible_text("Audi")
print(s1.all_selected_options)
print(s1.options)
print(s1.first_selected_option)
s1.deselect_all()
driver.close()
