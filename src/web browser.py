"""
 *   Created by PyCharm Professional, 2020
 *   User: nmn-gupta
 *   Date: 11/04/20
 *   Time: 10:44 PM

"""


import webbrowser
from tkinter import *


def openGoogle():
    webbrowser.open("http://www.google.com", new=0, autoraise=True)


def openAmazon():
    webbrowser.open("http://www.amazon.in", new=0, autoraise=True)


def openYoutube():
    webbrowser.open("http://www.youtube.com", new=0, autoraise=True)


def openFlipkart():
    webbrowser.open("http://www.flipkart.in", new=0, autoraise=True)


def openFacebook():
    webbrowser.open("http://www.facebook.com", new=0, autoraise=True)


def openTwitter():
    webbrowser.open("http://www.twitter.com", new=0, autoraise=True)


def openInstagram():
    webbrowser.open("http://www.instagram.com", new=0, autoraise=True)


root = Tk()
root.geometry("350x150")
root.title("All in one browser")
root.configure(background="black")
root.resizable(0, 0)
btn0 = Button(root, text="Google", font=('arabic', 12, 'bold'), width=10, command=openGoogle).place(x=20, y=20)
btn1 = Button(root, text="Instagram", font=('arabic', 12, 'bold'), width=10, command=openInstagram).place(x=220, y=20)
btn2 = Button(root, text="Facebook", font=('arabic', 12, 'bold'), width=10, command=openFacebook).place(x=220, y=60)
btn3 = Button(root, text="Flipkart", font=('arabic', 12, 'bold'), width=10, command=openFlipkart).place(x=120, y=60)
btn4 = Button(root, text="Twitter", font=('arabic', 12, 'bold'), width=10, command=openTwitter).place(x=120, y=60)
btn5 = Button(root, text="Youtube", font=('arabic', 12, 'bold'), width=10, command=openYoutube).place(x=20, y=60)
btn6 = Button(root, text="Amazon", font=('arabic', 12, 'bold'), width=10, command=openAmazon).place(x=120, y=20)
root.mainloop()
