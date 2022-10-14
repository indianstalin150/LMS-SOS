from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pywhatkit
from datetime import datetime, timedelta
import datetime
driver= webdriver.Edge(executable_path=r"C:\\Users\\harin\\OneDrive\\Documents\\Ai-Ds prjects\\msedgedriver.exe")
driver.get("https://moodle.kluniversity.in/login/index.php")
time.sleep(3)
driver.find_element(By.NAME,'username').send_keys("2100080201")
driver.find_element(By.NAME,'password').send_keys("Kalyan@03.")
driver.find_element(By.ID,'loginbtn').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,'slicon-bell').click()
time.sleep(2)
l=driver.find_element(By.LINK_TEXT,"View full notification")
l.click()
time.sleep(3)
notifl,datal=[],[]
a=driver.find_elements(By.CLASS_NAME,"content")
print("list is:",a)
time.sleep(3)
final=''
for i in a:
    time.sleep(1)
    notifl.append(i)
    works=driver.find_elements(By.TAG_NAME,"tr")
    time.sleep(3)
    for work in works:
        datal.append(work.text)
        final=work.text+" "
    i.click()
    time.sleep(2)
print("notifications:",notifl)
print(datal)
datal1=''.join(datal)
print(datal1)
delta = timedelta(seconds=30) # For adding 30 seconds to current time to send message
ctime=datetime.datetime.now()
msg_time = ctime + delta 
pywhatkit.sendwhatmsg("+918919076694", datal1, int(msg_time.hour),int(msg_time.minute),int(msg_time.second))












