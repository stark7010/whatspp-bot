from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
#this python script is used to send 100s of spam messages to someone on whatapp for fun XD
contact_name="name" #replace name with the name os the person as saved in your contact list
driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Desktop\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
a = input("Press enter after scaning QR code") #scan the QR code from the whatsapp pp
inp_xpath_search = " //div[@class='_3FRCZ copyable-text selectable-text']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact_name)
time.sleep(2)
user = driver.find_element_by_xpath("//span[@title='{}']".format(contact_name))
user.click()
chat = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(500): #replace 500 with the number of times you want to send the message
    chat.send_keys("Guess who learned to automate whatsapp using Python") #replace this with whatever message you want to send
    chat.send_keys(Keys.RETURN)

#Hope you enjoyed using this fun bot!
#future work: 1)send the messages at a specified time
#             2)Remove the need to scan the QR code everytime the script is used