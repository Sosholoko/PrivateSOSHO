from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import tkinter as tk
from tkinter import *
from tkmacosx import Button as button


class TwitterBot:
    def __init__(self, username, password):
        print("Username =", username, "   Password =", password)
        self.username = username
        self.password = password
        
    def set_credentials(self):
        self.username = entry_user.get()
        self.password = entry_pass.get()
        print("Username =", self.username, "   Password =", self.password)

    def open_br(self):
        self.bot = webdriver.Firefox()
        
    def end_br(self):
        self.bot.quit()
    
    def login(self):
        bot = self.bot
        bot.get("http://twitter.com/login/")
        time.sleep(3)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)



    def like_tweet(self, hashtag):
            bot = self.bot
            bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
            time.sleep(3)
            for i in range(1,8):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
                tweets = bot.find_elements_by_class_name('tweet')
                tweetLinks = [i.get_attribute('href') for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
                filteredTweet = list(filter(lambda x: 'status' in x,tweetLinks))
                print(filteredTweet)

                for link in filteredTweet:
                    bot.get(link)
                    time.sleep(5)
                    if drop2_var.get() == "Retweet":
                        try:
                            bot.find_element_by_xpath("//div[@data-testid='retweet']").click()
                            bot.find_element_by_xpath("//div[@data-testid='retweetConfirm']").click()
                            time.sleep(3)
                        except Exception as ex:
                            time.sleep(10)
                    elif drop2_var.get() == "Likes":
                        bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(3)



# def create_bot(event=None):
#         sasha = TwitterBot(entry_user.get(), entry_pass.get())
#         print("started bot")

sasha = TwitterBot("MikeFis00475522", "sasha0408")

root = tk.Tk()


HEIGHT = 800
WIDTH = 400



#FUNCTIONS CLEARING ENTRY


def del_value(event): # note that you must include the event as an arg, even if you don't use it.
    entry.delete(0, "end")
    return None
def del_value_user(event): # note that you must include the event as an arg, even if you don't use it.
    entry_user.delete(0, "end")
    return None
def del_value_pass(event): # note that you must include the event as an arg, even if you don't use it.
    entry_pass.delete(0, "end")
    return None


def ex():
    root.quit()

#PROGRAM SETTINGS


root.title("Social Bot")
root.minsize(400, 800)
#root.iconbitmap("/Users/sashakharoubi/Desktop/BOOTCAMP/Week 9/Day 2/image/logo.ico")
root.config(background="#66b3ff")

canvas = tk.Canvas(root, height= HEIGHT, width = WIDTH, bd=0, highlightthickness = 0)
canvas.pack()

# background_image = tk.PhotoImage(file = 'blue.png')
# background_label = tk.Label(root, image =background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

#MAINFRAME

frame = tk.Frame(root, bg="#222f3e")
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


#SUBPART FRAME

lower_frame = tk.Frame(root, bg="#E9E9E9", bd=0, highlightthickness = 0, relief="sunken")


#DROPDOWN MENU OPTIONS

OPTIONS = [
    "Twitter",
    "Instagram(not working)"
]

OPTIONS2 = [
    "Likes",
    "Retweet"
]

entry_txt = tk.Label(lower_frame, text="Welcome to Social Bot\n\nChoose an action to execute", font=("Montserrat", 15), bg="#E9E9E9", fg="black")
entry_txt.pack(expand = "yes")


#DROPDOWN MENU

drop_var = StringVar(lower_frame)
drop_var.set(OPTIONS[0]) 
drop2_var = StringVar(lower_frame)
drop2_var.set(OPTIONS2[0]) 


drop = OptionMenu(lower_frame, drop_var, *OPTIONS)
drop.config(fg="black")
drop.pack()
drop2 = OptionMenu(lower_frame, drop2_var, *OPTIONS2)
drop2.config(fg="black")
drop2.pack()


#ENTRIES


entry = tk.Entry(lower_frame, bg="white", fg='black', bd=0)
entry.insert(0, "-->Topic to like or retweet")
entry.bind("<Button-1>", del_value)
entry.pack(expand = "yes")

entry_user = tk.Entry(lower_frame, bg="white", fg='black', bd=0)
entry_user.insert(0, "----Type Your Username---")
entry_user.bind("<Button-1>", del_value_user)
entry_user.pack(expand = "yes")
#entry_user.bind("<Return>", create_bot)

entry_pass = tk.Entry(lower_frame, bg="white", fg='black', bd=0)
entry_pass.insert(0, "----Type Your Password---")
entry_pass.bind("<Button-1>", del_value_pass)
entry_pass.pack(expand = "yes")
#entry_pass.bind("<Return>", create_bot)




#BUTTONS

button_confirm = button(lower_frame, text="Confirm", bg="white", fg="black", command=sasha.set_credentials)
button_confirm.pack(pady=25, side = 'top')

button_open = button(lower_frame, text="Open Browser", bg="white", fg="black", command= sasha.open_br)
button_open.pack(pady=25, side = 'top')

button_log = button(lower_frame, text="LOG IN", bg='#54a0ff', fg="white", command =sasha.login, bd=0, highlightthickness = 0)
button_log.pack(pady=25, side = 'left')

button_launch = button(lower_frame, text="START", bg='#1dd1a1', fg="white", relief="flat", command = lambda: sasha.like_tweet(entry.get()), bd=0, highlightthickness = 0)
button_launch.pack(pady=25, side = 'right')

button_stop = button(lower_frame, text="STOP", bg="#ff6b6b", fg="white", command= sasha.end_br)
button_stop.pack(pady=25, side = 'bottom')

button_exit = button(lower_frame, text="Exit", bg ="white", fg="black", command= ex)
button_exit.pack(side = 'bottom')



lower_frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.8)


#TITLE


label = tk.Label(frame, text="S O C I A L    B O T", font=("Montserrat", 25), bg="white", fg="#222f3e")
label.pack(side="top", fill ="both")




root.mainloop()