from gui import *
from holidays import Holidays

def main():
    window = Window()
    window.create()
    window.handler.mainloop()

    holiday = Holidays()
    example = holiday.get(window.datefrom)
    print(example)

if __name__ == "__main__":
    main()
