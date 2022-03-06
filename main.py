from gui import *
from holidays import Holidays


HOLIDAYS = ["Wielkanoc", "Nowy Rok", "Boże Ciało", "Święto Pracy"]

    window = Window()
    window.create()
    window.handler.mainloop()

    holiday = Holidays(window.datefrom, window.dateto, HOLIDAYS)

if __name__ == "__main__":
    main()
