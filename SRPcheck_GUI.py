import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
#selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

#Selenium chromedriver options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

#TK window
win = Tk()
win.title("SRP Irrigation Schedule Checker")
###Window Width x Height
win.geometry("300x200")

#variables
filename = StringVar()
filename.set("chromedriver.exe")
account = StringVar()
account.set("xxxxxxx")
msg = StringVar()
msg.set("Search for your posted irrigation time")
prog = IntVar()
prog.set(0)



def getIt():  
    prog.set(0)
    msg.set("Let's go!")
    win.update()  
    if filename.get() == "chromedriver.exe":
        messagebox.showinfo( "Warning!","Please set path for chromedriver!")

    elif account.get() == "xxxxxxx":
        messagebox.showinfo( "Warning!","Please input SRP account number!")

    else:
        prog.set(10)
        prog.set(20)
        msg.set( "Looking up site.")
        win.update()
        #set chromedriver path
        PATH = filename.get()
        driver = webdriver.Chrome(PATH, options=options)

        try:
            driver.get("https://water.srpnet.com/quick-view/schedule")

            try:
                search = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "mat-input-0")))
                prog.set(50)
                msg.set('Inputing account info..')
                win.update()

                search.send_keys(account.get())
                search.send_keys(Keys.RETURN)
                prog.set(75)
                msg.set("Looking up account...")
                win.update()

                try:
                    info = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "schedule-info")))
                    prog.set(90)
                    msg.set("Schedule found....")
                    win.update()
                    prog.set(100)
                    msg.set(info.text)

                except:
                    msg.set('Account could not be found, verify Acct.#.')
                    win.update()
            
            except:
                msg.set('Account info could not be entered.')
                win.update()

        except:
            msg.set('Site could not be reached.')
            win.update()        
            
        finally:            
            driver.quit()
            
def getPath():
    filename.set(filedialog.askopenfilename(initialdir = "/Downloads",
                                          title = "Select a File",
                                          filetypes = (("Application",
                                                        "*.exe*"),
                                                        ("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*"))))
    print("got chromedriver PATH")
    print(filename.get())


l1 = Label(win, text="Enter SRP account #").place(relx=.5, rely=.05, anchor= CENTER)
input1 = Entry(win, textvariable=account, justify=CENTER).place(relx=.5, rely=.15, anchor= CENTER)
l2 = Label(win, text="Set path for chromedriver:").place(relx=.5, rely=.35, anchor= CENTER)
input2 = Entry(win, textvariable=filename).place(relx=.5, rely=.45, anchor= CENTER)
b = Button(win, text="Get Schedule", command=getIt).place(relx=.5, rely=.65, anchor= CENTER)
b2 = Button(win, text="PATH:", command=getPath).place(relx=.15, rely=.45, anchor= CENTER)
l3 = Label(win, textvariable=msg).place(relx=.5, rely=.8, anchor= CENTER)

#Progress bar
progress = Progressbar(win, orient = HORIZONTAL, variable=prog, 
              length = 100, mode = 'determinate').place(relx=.5, rely=.9, anchor=CENTER, relwidth=.8)


print("still working")


win.mainloop()
