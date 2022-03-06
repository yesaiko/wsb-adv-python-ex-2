from tkinter import *
from tkinter import messagebox
from datetime import datetime

class Window:
    handler = Tk()
    datefrom = 0
    dateto = 0

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

        Button(self.handler, text="Generate chart", width=20, bg="pink", fg="black", command=lambda: self.submit(e_datefrom, e_dateto)).place(x=180, y=250)

    def submit(self, datefrom, dateto):
        datefrom = datefrom.get()
        dateto = dateto.get()
        if not self.validate(datefrom) or not self.validate(dateto):
            print("Wprowadz poprawna date")
        self.handler.destroy()
        self.datefrom = datefrom
        self.dateto = dateto

    def validate(self, date):
        try:
            date = int(date)
        except:
            return False
        if date < 2013 and date > datetime.now().year:
            print(datetime.now().year)
            return False
        return True

    

    

    




