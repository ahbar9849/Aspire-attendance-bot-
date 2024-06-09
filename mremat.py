import tkinter
from tkinter import *
import tkinter.ttk as ttk
import time
import requests
from tkinter import messagebox
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import concurrent.futures
import pyautogui
import threading
from tkinter import ttk
import tkinter as ttk
import tkinter as tk
import tkinter.ttk as ttk 
import customtkinter as CTk
from PIL import ImageTk, Image 

from CTkMessagebox import CTkMessagebox
import customtkinter
application=customtkinter.CTk()
x_axis=application.winfo_screenwidth()
y_axis=application.winfo_screenheight()
application.geometry(f"{x_axis}x{y_axis}")
application.after(1,lambda:application.state('zoomed'))
application.title('lords attendence bot')
mainframe=customtkinter.CTkFrame(application, width=x_axis,height=y_axis,fg_color='#f7b04d',border_color='#f29727',border_width=6)
mainframe.place(x=0,y=0)
# bg = PhotoImage(file = "lords_bg.png") 
# mainframe= Label( application, image = bg) 
# mainframe.place(relx = 0.5, rely=0.5) 
image1 = Image.open("mrrrr.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=200, y=200)
application_banner_lords=customtkinter.CTkLabel(mainframe,font=('Old English Text MT',52,'bold','underline'),text='malla reddy engineering college and management',text_color='#201f7a')
application_banner_lords.place(relx=0.231-0.13,rely=0.010)
application_banner_attendence=customtkinter.CTkLabel(mainframe,font=('Old English Text MT',82,'bold','underline'),text='Attendance Bot',text_color='#201f7a')
application_banner_attendence.place(relx=0.180,rely=0.044)
application_banner_bot=customtkinter.CTkLabel(mainframe,font=('times new roman',34,'bold','underline'),text='Enter Your Roll no:',text_color='#201f7a')
application_banner_bot.place(relx=0.034,rely=0.24)
get_box_value1=tkinter.StringVar()
get_box_value2=tkinter.StringVar()
get_box_value3=tkinter.StringVar()
get_box_value4=tkinter.StringVar()
# get_box_value4=tkinter.StringVar()

get_box_value1.set('')
get_box_value2.set('')
get_box_value3.set('')
get_box_value4.set('')

input_box=customtkinter.CTkEntry(mainframe,textvariable=get_box_value1,border_width=4,width=377,height=42,font=('Calibri',25,'bold'),placeholder_text='enter your roll no')
input_box.place(relx=0.02,rely=0.27)
input_box=customtkinter.CTkEntry(mainframe,textvariable=get_box_value2,border_width=4,width=377,height=42,placeholder_text='Enter your roll no',text_color='black',font=('Calibri',25,'bold'))
input_box.place(relx=0.02,rely=0.30)
input_box=customtkinter.CTkEntry(mainframe,textvariable=get_box_value3,border_width=4,width=377,height=42,placeholder_text='Enter your roll no',font=('Calibri',25,'bold'))
input_box.place(relx=0.02,rely=0.33)
input_box=customtkinter.CTkEntry(mainframe,textvariable=get_box_value4,border_width=4,width=377,height=42,placeholder_text='Enter your roll no',font=('Calibri',25,'bold'))
input_box.place(relx=0.02,rely=0.36)

box_ka_data=tkinter.StringVar()

text_box=customtkinter.CTkTextbox(mainframe,width=500,height=500,fg_color='#ebf6fa',text_color='black',border_color='#201f7a',border_width=4,font=("Calibri",20,'bold'))
text_box.place(x=575,y=230)

def get_details():
	data=[get_box_value1.get(),get_box_value2.get(),get_box_value3.get(),get_box_value4.get()]
	# option=Options()
	# option.add_argument('--headless')
	driver=webdriver.Chrome()
	url = "https://mrem.schoolsera.com/esaap/index.action"
	for x in data:
	    driver.get(url)
	    time.sleep(4)
	    c=driver.find_element(By.XPATH,'//*[@id="loginuser1"]').send_keys(x)
	    d=driver.find_element(By.XPATH,'//*[@id="loginpassword1"]').send_keys(x)
	    time.sleep(3)
	    e=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr/td/div/form/table[4]/tbody/tr/td[1]/table/tbody/tr/td/div').click()
	    time.sleep(3)
	    f=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/button/span[1]').click()
	    time.sleep(3)
	    g=driver.find_element(By.XPATH,'//*[@id="menubar0"]').click()
	    time.sleep(2)
	    h=driver.find_element(By.XPATH,'//*[@id="ui-id-2"]').click()
	    time.sleep(2)
	    i=driver.find_element(By.XPATH,'//*[@id="ui-id-3"]').click()
	    time.sleep(2)
	    j=driver.find_element(By.XPATH,'//*[@id="fee101_infoList"]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr[16]/td[3]/table/tbody/tr[2]/td/p/span').text
	    k=driver.find_element(By.XPATH,'//*[@id="welcome"]/table/tbody/tr/td[1]/b').text
	    data=f"Name: {k}\nAttendance: {j}"
	    print(data)
	    text_box.insert('end',f'{data}')
	    text_box.insert('end','\n\n')
	    logout=driver.find_element(By.XPATH,'//*[@id="welcome"]/table/tbody/tr/td[1]/a/b').click()
		



		



	

			
def run_chrome():
	threading.Thread(target=get_details).start()


btn_get_details=customtkinter.CTkButton(mainframe,command=run_chrome,hover_color='#282829',text_color='#2ebde8',fg_color='#ebf6fa',text='Get details',font=('Algerian',20,'bold','underline',),width=240,)
btn_get_details.place(relx=0.182,rely=0.38)

btn_get_details.configure(cursor='')
input_box.configure(textvariable=get_box_value1)
input_box.configure(textvariable=get_box_value2)
input_box.configure(textvariable=get_box_value3)
input_box.configure(textvariable=get_box_value4)


# btn_get_results=customtkinter.CTkButton(mainframe,command=run_chrome,hover_color='#282829',text_color='#0b7331',fg_color='#ebf6fa',text='Get results',font=('Algerian',20,'bold','underline',),width=240,)
# btn_get_results.place(relx=.172,rely=0.43)

def delete_info():
	text_box.delete(1.0,'end')
btn_del_details=customtkinter.CTkButton(mainframe,command=delete_info,hover_color='black',text_color='red',fg_color='#ebf6fa',text='Delete Info',font=('Algerian',20,'bold','underline',),width=240,)
btn_del_details.place(relx=0.26,rely=0.38)

# btn_get_details.configure(cursor='heart')


application.mainloop()