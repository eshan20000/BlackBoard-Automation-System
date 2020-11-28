import sys
import time
import tkinter as tk
import urllib.request as urllib2
import xml.dom.minidom
from datetime import datetime
from tkinter import messagebox

import schedule
import selenium.common.exceptions as EX
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def timetable_Saving():
    print(
        "Please download and save your timetable from UIMS in xml format, rename it to 'TimeTable.xml' and save it in "
        "the same folder as the program.")
    # XML Parser

    ans = input("Have you done the above step? Yes or No\n")

    if ans == "No":
        print("Do it right now before proceeding")
        sys.exit("Do the above task!")
    else:
        print("Okays... lets get started!")

    doc = xml.dom.minidom.parse("TimeTable.xml")

    allTags = doc.getElementsByTagName("TimingId")

    allTimings = []
    for x in allTags:
        allTimings.append(x.getAttribute("TimingId"))

    # for x in allTimings:
    #     pass
    #     print(x[:5])  # Start Time
    # print(x[-8:])           # End Time

    allDayNo = doc.getElementsByTagName("DayNo")
    # print("%d TimingId:" % allDayNo.length)

    allDays = []
    global allClasses
    allClasses = []

    for x in allDayNo[:6]:
        allDays.append(x.getAttribute("DayNo"))

    # for x in allDays:
    #     print(x)

    for x in allDayNo:
        allClasses.append(x.getAttribute("CourseCode")[:7])

    # Saving data of Lectures by Timing

    global first
    global second
    global third
    global fourth
    global fifth
    global sixth
    global seventh

    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    sixth = []
    seventh = []

    for x in allClasses[:6]:
        first.append(x)

    for x in allClasses[6:12]:
        second.append(x)

    for x in allClasses[12:18]:
        third.append(x)

    for x in allClasses[18:24]:
        fourth.append(x)

    for x in allClasses[24:30]:
        fifth.append(x)
    if len(allClasses) > 30:
        for x in allClasses[30:36]:
            sixth.append(x)
    if len(allClasses) > 36:
        for x in allClasses[36:42]:
            seventh.append(x)

    temp = first

    # Monday
    schedule.every().monday.at("09:50").do(class_joiner, var=first[0])
    schedule.every().monday.at("10:50").do(class_joiner, var=second[0])
    schedule.every().monday.at("11:50").do(class_joiner, var=third[0])
    schedule.every().monday.at("12:35").do(class_joiner, var=fourth[0])
    schedule.every().monday.at("13:35").do(class_joiner, var=fifth[0])
    if len(allClasses) > 30:
        schedule.every().monday.at("14:35").do(class_joiner, var=sixth[0])
    if len(allClasses) > 36:
        schedule.every().monday.at("15:35").do(class_joiner, var=seventh[0])

    # Tuesday
    schedule.every().tuesday.at("09:50").do(class_joiner, var=first[1])
    schedule.every().tuesday.at("10:50").do(class_joiner, var=second[1])
    schedule.every().tuesday.at("11:50").do(class_joiner, var=third[1])
    schedule.every().tuesday.at("12:35").do(class_joiner, var=fourth[1])
    schedule.every().tuesday.at("13:35").do(class_joiner, var=fifth[1])
    if len(allClasses) > 30:
        schedule.every().tuesday.at("14:35").do(class_joiner, var=sixth[1])
    if len(allClasses) > 36:
        schedule.every().tuesday.at("15:35").do(class_joiner, var=seventh[1])

    # Wednesday
    schedule.every().wednesday.at("09:50").do(class_joiner, var=first[2])
    schedule.every().wednesday.at("10:50").do(class_joiner, var=second[2])
    schedule.every().wednesday.at("11:50").do(class_joiner, var=third[2])
    schedule.every().wednesday.at("12:35").do(class_joiner, var=fourth[2])
    schedule.every().wednesday.at("13:35").do(class_joiner, var=fifth[2])
    if len(allClasses) > 30:
        schedule.every().wednesday.at("14:35").do(class_joiner, var=sixth[2])
    if len(allClasses) > 36:
        schedule.every().wednesday.at("15:35").do(class_joiner, var=seventh[2])

    # Thursday
    schedule.every().thursday.at("09:50").do(class_joiner, var=first[3])
    schedule.every().thursday.at("10:50").do(class_joiner, var=second[3])
    schedule.every().thursday.at("11:50").do(class_joiner, var=third[3])
    schedule.every().thursday.at("12:35").do(class_joiner, var=fourth[3])
    schedule.every().thursday.at("13:35").do(class_joiner, var=fifth[3])
    if len(allClasses) > 30:
        schedule.every().thursday.at("14:35").do(class_joiner, var=sixth[3])
    if len(allClasses) > 36:
        schedule.every().thursday.at("15:35").do(class_joiner, var=seventh[3])

    # Friday
    schedule.every().friday.at("09:50").do(class_joiner, var=first[4])
    schedule.every().friday.at("10:50").do(class_joiner, var=second[4])
    schedule.every().friday.at("11:50").do(class_joiner, var=third[4])
    schedule.every().friday.at("12:35").do(class_joiner, var=fourth[4])  # update
    schedule.every().friday.at("13:35").do(class_joiner, var=fifth[4])
    if len(allClasses) > 30:
        schedule.every().friday.at("14:35").do(class_joiner, var=sixth[4])
    if len(allClasses) > 36:
        schedule.every().friday.at("15:35").do(class_joiner, var=seventh[4])

    # Saturday
    schedule.every().saturday.at("09:50").do(class_joiner, var=first[5])
    schedule.every().saturday.at("10:50").do(class_joiner, var=second[5])
    schedule.every().saturday.at("11:50").do(class_joiner, var=third[5])
    schedule.every().saturday.at("12:35").do(class_joiner, var=fourth[5])
    schedule.every().saturday.at("13:35").do(class_joiner, var=fifth[5])
    if len(allClasses) > 30:
        schedule.every().saturday.at("14:35").do(class_joiner, var=sixth[5])
    if len(allClasses) > 36:
        schedule.every().saturday.at("15:35").do(class_joiner, var=seventh[5])


def browser_Check():
    print("You need to use Chrome for this to work)")
    global path

    path = input(
        "Enter the Path of the chromedriver.exe or the geckodriver.exe which is provided with the program (Ex: "
        "C:/Users/Desktop/TheProxinator/driver/chromedriver.exe) Just drag and drop it into the console.")

    global username
    global password

    username = input("PLease enter your username (your UID): ")
    password = input("Please enter the password: ")


def start(var):
    global driver
    opt = Options()
    opt.add_argument("user-data-dir=selenium")
    prefs = {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    }
    opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=opt, executable_path=path)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.70);')
    driver.get("https://cuchd.blackboard.com/ultra/course")
    driver.implicitly_wait(10)
    # driver.find_element_by_class_name("consent-footer").find_element_by_tag_name("button").click()
    print("Webpage Opened!")

    driver.implicitly_wait(10)
    try:
        if driver.find_element_by_name('user_id').is_displayed():
            driver.find_element_by_name("user_id").send_keys(username)
            driver.implicitly_wait(5)
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_name("password").send_keys(Keys.TAB)
            driver.find_element_by_id("entry-login").send_keys(Keys.ENTER)
            try:
                errorMsg = driver.find_element_by_id("loginErrorMessage").text
                print("Error: " + errorMsg)
                exit(0)
            except EX.NoSuchElementException as error:
                print("Error: ", error)
            finally:
                pass
            print("Logged In!")
        elif driver.find_element_by_xpath('//*[@id="main-heading"]').text == "Courses":
            join_class(var)
        else:
            pass
    except:
        pass
    driver.implicitly_wait(5)
    return


def join_class(subject):
    # Clicking the Subject
    driver.implicitly_wait(15)
    sub = driver.find_element_by_xpath('*//div[contains(text(),"' + subject + '")]')
    sub = sub.find_element_by_xpath('..')
    sub.find_element_by_tag_name('a').send_keys(Keys.ENTER)

    # join session button code

    driver.implicitly_wait(15)
    driver.find_element_by_id("sessions-list-dropdown").send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="sessions-list"]/li[2]/a').send_keys(Keys.ENTER)

    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(10)

    # driver.find_element_by_xpath('//*[contains(text(), "Audio is")]').click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath('//*[contains(text(), "Video is")]').click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/div/div[4]/button').click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath('//*[@id="tutorial-dialog-tutorials-menu-learn-about-tutorials-menu-close"]').click()

    while True:
        try:
            driver.find_element_by_xpath('//*[@id="connect-status-connecting"]/div/div/button').send_keys(Keys.ENTER)
        except:
            pass

        if datetime.now().hour == 10 and datetime.now().minute == 45 or datetime.now().hour == 11 and datetime.now().minute == 45 or datetime.now().hour == 12 and datetime.now().minute == 45 or datetime.now().hour == 13 and datetime.now().minute == 30 or datetime.now().hour == 14 and datetime.now().minute == 30 or datetime.now().hour == 15 and datetime.now().minute == 30 or datetime.now().hour == 16 and datetime.now().minute == 30:
            driver.quit()
            # driver.implicitly_wait(10)
            # driver.switch_to.window(driver.window_handles[0])
            # driver.implicitly_wait(15)
            # driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/div/div[2]/button').send_keys(Keys.ENTER)
            # driver.implicitly_wait(20)
            break
        if datetime.now().hour == 16 and datetime.now().minute == 30:
            try:
                driver.quit()
            except:
                pass
            sys.exit("Thank You for using my Program!")


def class_joiner(var):
    print(var)
    if var == "":
        print("No Class")
    else:
        start(var)
        join_class(var)


def main():
    timetable_Saving()
    browser_Check()

    while True:
        schedule.run_pending()
        time.sleep(1)


def connection_check():
    try:
        urllib2.urlopen("https://cuchd.blackboard.com/", timeout=5)
        return True
    except urllib2.URLError as err:
        return False


def get_date():
    a = datetime.today().strftime('%Y%m%d')
    return a


root = tk.Tk()
root.withdraw()

if connection_check():
    limit = 20210301  # year/month/date
    current = int(get_date())
    if current < limit:
        main()
    else:
        messagebox.showinfo("Sorry ", "Your program has expired!")
else:
    messagebox.showerror("Please ", "Check your Internet Connection!")
