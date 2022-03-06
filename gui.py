from tkinter import *
from tkinter import messagebox

class Window:
    handler = Tk()

    def create(self):
        self.handler.geometry("500x350")
        self.handler.title("Holidays weather")

        l_title = Label(self.handler, text="Weather during holidays", width=27, font=("Courier", 15, "italic"))
        l_title.place(x=90, y=60)
        
        l_datefrom = Label(self.handler, text="Date from:", width=20, font=("bold", 10))
        l_datefrom.place(x=80, y=130)

        l_dateto = Label(self.handler, text="Date to:", width=20, font=("bold", 10))
        l_dateto.place(x=73, y=180)

        e_datefrom = Entry(self.handler)
        e_datefrom.place (x=240, y=130)

        e_dateto = Entry(self.handler)
        e_dateto.place (x=240, y=180)

        Button(self.handler, text="Generate chart", width=20, bg="pink", fg="black", command=self.submit).place(x=180, y=250)

    def submit(self):
        



