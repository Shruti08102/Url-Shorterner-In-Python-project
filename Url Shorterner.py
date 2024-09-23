from tkinter import *
import pyshorteners
import getpass
database = {"shruti": "ak@8", "kanchan": "ka@2"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")

def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
root.title(" URL Shortner")
root.geometry("800x350")
root.resizable(False, False)
root.config(background="#ADD8EC")

# Declare variables
url = StringVar()
shorturl = StringVar()

# Design labels
Label(root, text="URL Shortner", bg="#ffffe0", fg="#000000", font="verdana 22 ").place(x=80, y=10)
Label(root, bg="#ffffe0",fg="#E74C3C",font="verdana 12 ").place(x=15, y=50)

# Accepting URL as a Input
Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold",padx=2, pady=2).place(x=7, y=100)
Entry(root, textvariable=url, font="verdana 12", width=60).place(x=7, y=120)

# Creating button to give a call for convert function
Button(root, text="Convert...", bg="#fdde6c", fg="#000", font="verdana 12 "
        , command=convert, relief=GROOVE).place(x=7, y=180)

# Displaying shortened URL
Label(root, text="Shortened URL - Copy & Paste in browser", bg="#2C3E50", fg="#EAECEE"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)

root.mainloop()
