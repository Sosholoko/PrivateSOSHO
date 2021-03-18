import sqlite3, hashlib
import time 
from tkinter import *
from tkmacosx import Button as button
from tkinter import simpledialog
from functools import partial


#Database

with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

#PopUP

def popup(text):
    answer = simpledialog.askstring("input string", text)
    
    return answer




window = Tk()

window.title("Password Vault")
window.config(background="#192a56")

def hashPassword(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()

    return hash

def first_screen():
    window.geometry("400x260")
    
    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor="center")
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack(pady = 20)
    txt.focus()
    
    lbl1 = Label(window, text = "Re-enter Password to confirm")
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack(pady = 20)
    

    lbl2 = Label(window)
    lbl2.pack()

    def save_password():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode("utf-8"))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

    

            passwordVault()
        else:
            lbl2.config(text = "Passwords do not match")

    btn = button(window, text = "Save", command = save_password)
    btn.pack(pady = 15)


def login_screen():
    window.geometry("350x180")

    lbl = Label(window, text="Enter Master Password", bg="#192a56", fg="white", font= 12)
    lbl.config(anchor="center", font=("Arial", 20))
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack(pady = 20)
    txt.focus()
    
    lbl1 = Label(window, bg="#192a56", fg = "white")
    lbl1.config(text = "Welcome Back Sasha", fg ="green")
    lbl1.pack()

    def get_masterPassword():
        checkhashedPassword = hashPassword(txt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkhashedPassword)])
        print(checkhashedPassword)
        return cursor.fetchall()

    def checkPassword():
        match = get_masterPassword()

        print(match)
        

        if match:
            lbl1.config(text = "Welcome Back Sasha", fg = "green")
            passwordVault()
        else:
            txt.delete(0, "end")
            lbl1.config(text ="Wrong Password", fg= "red")

    btn = button(window, text = "Confirm", command = checkPassword, bg="#1dd1a1", fg="white")
    btn.pack(pady = 15)


def passwordVault():
    for Widget in window.winfo_children():
        Widget.destroy()

    def addEntry():
        text1 = "Website"
        text2 = "Username"
        text3 = "Password"

        website = popup(text1)
        username = popup(text2)
        password = popup(text3)

        insert_fields = """INSERT INTO vault(website, username, password)
        VALUES(?, ?, ?)"""

        cursor.execute(insert_fields, (website, username, password))
        db.commit()

        passwordVault()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        passwordVault()


    window.geometry("930x580")

    

    lbl = Label(window, text = "Password Vault", bg="#192a56", fg = "white")
    lbl.config(font=("Modern", 25))
    lbl.grid(column=1, padx = 30, pady= 20)

    btn = button(window, text = "Add", command = addEntry, bg="#0097e6", fg = "white")
    btn.grid(column=1, pady=10)

    lbl1 = Label(window, text = "Website",bg="#192a56", fg = "white")
    lbl1.config(font=("Arial", 25))
    lbl1.grid(row=2, column=0, padx=80, pady = 80)
    lbl2 = Label(window, text = "Username", bg="#192a56", fg = "white")
    lbl2.config(font=("Arial", 25))
    lbl2.grid(row=2, column=1, padx=80)
    lbl3 = Label(window, text = "Password", bg="#192a56", fg = "white")
    lbl3.config(font=("Arial", 25))
    lbl3.grid(row=2, column=2, padx=80)

    cursor.execute("SELECT * FROM vault")
    if (cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            lbl1 = Label(window, text = (array[i][1]), font = 12, bg="#192a56", fg = "white")
            lbl1.grid(column=0, row=i+3, )
            lbl2 = Label(window, text = (array[i][2]), font = 12, bg="#192a56", fg = "white")
            lbl2.grid(column=1, row=i+3, )
            lbl3 = Label(window, text = (array[i][3]), font = 12, bg="#192a56", fg = "white")
            lbl3.grid(column=2, row=i+3, )

            btn = button(window, text="Delete", command = partial(removeEntry, array[i][0]), bg="#ff7675", fg = "white")
            btn.grid(column=3, row=i+3, pady= 10)

            i = i+1

            cursor.execute("SELECT * FROM vault")
            if (len(cursor.fetchall()) <= i):
                break

cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    login_screen()
else:
    first_screen()



window.mainloop()