import twint
import forms
import flask
import tkinter as tk
from tkinter import *
from tkmacosx import Button as button


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/tweet", methods=["GET", "POST"])
def search():
    form = forms.Twitter()
    tweets = []
    # return flask.render_template

    if flask.request.method == "POST":
        if form.validate_on_submit():
            subject = form.subject.data
            location = form.location.data
            print(subject)
            c = twint.Config()
            c.Search = subject
            c.Near = location
            c.Limit = 20
            c.Popular_tweets = True
            result = twint.run.Search(c)
            
        return flask.redirect('/')
    
    return flask.render_template("search.html", form=form)
# search = input("What ? ")
# city = input("Where ? ")






app.run(port=5000, debug=True)

# root = tk.Tk()


# HEIGHT = 800
# WIDTH = 400

# root.title("Social Bot")
# root.minsize(400, 800)

# canvas = tk.Canvas(root, height= HEIGHT, width = WIDTH, bd=0, highlightthickness = 0)
# canvas.pack()

# frame = tk.Frame(root, bg="#222f3e")
# frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

# lower_frame = tk.Frame(root, bg="#E9E9E9", bd=0, highlightthickness = 0, relief="sunken")

# entry = tk.Entry(frame, bg="white", fg='black', bd=0)
# entry.insert(0, "-->Topic to search for")
# entry.pack(expand = "yes")

# entry2 = tk.Entry(frame, bg="white", fg='black', bd=0)
# entry2.insert(0, "-->Location of topic search")
# entry2.pack(expand = "yes")

# button_confirm = button(frame, text="Confirm", bg="white", fg="black")
# button_confirm.pack(pady=25, side = 'top')



# root.mainloop()