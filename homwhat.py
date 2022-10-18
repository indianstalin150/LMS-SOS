from pickle import TRUE
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pywhatkit
from datetime import datetime, timedelta
import datetime
def openbrowser():
    driver= webdriver.Edge(executable_path=r"C:\\Users\\harin\\OneDrive\\Documents\\Ai-Ds prjects\\msedgedriver.exe")
    driver.get("https://moodle.kluniversity.in/login/index.php")
    driver.minimize_window()
    return driver

def fill_credentials(user_name,password):

    driver.maximize_window()
    username_xpath="//*[@id='username']"
    password_xpath="//*[@id='password']"
    login_button_xpath="//*[@id='loginbtn']"
    my_username=user_name
    my_password=password
    send_username=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    send_username.send_keys(my_username)
    send_password=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,password_xpath)))
    send_password.send_keys(my_password)
    login_button_click=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,login_button_xpath))).click()

def check_notifications():
    global list_notifications
    notification_bell_xpath="//*[@id='nav-notification-popover-container']"
    notification_Bell=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,notification_bell_xpath)))
    notification_Bell.click()
    view_full_notification_xpath="/html/body/nav/ul[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/a[2]"
    view_full_notification=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,view_full_notification_xpath)))
    view_full_notification.click()
    time.sleep(3)
    list_notifications=WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"content")))
    print("list is:",list_notifications)
if __name__ == "__main__":

    driver = openbrowser()
    user_name=input("give your LMS user name\n")
    password=input("give your LMS password\n")
    time.sleep(10)
    if user_name!='' and password!='':
        fill_credentials(user_name,password)
    notifl,datal=[],[]
    list_notifications=[]
    check_notifications()
    final,datal1='',[]
    def read_notifications():
        global list_notifications
        for i in list_notifications:
            notifl.append(i)
            works=WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME,"tr")))
            for work in works:
                datal.append(work.text)
            i.click() 
            time.sleep(1)
        time.sleep(2)
        print("notifications:",notifl)
        print("datal:",datal)
    read_notifications()
    datal1=''.join(datal)
    #delta = timedelta(seconds=57) For adding 30 seconds to current time to send message
    ctime=datetime.datetime.now()
    msg_time = ctime
    # pywhatkit.sendwhatmsg("+918919076694", datal1, int(msg_time.hour),int(msg_time.minute),int(msg_time.second), wait_time=50)
    pywhatkit.sendwhatmsg("+918919076694",datal1,int(msg_time.hour),int(msg_time.minute)+1)
    time.sleep(3)

