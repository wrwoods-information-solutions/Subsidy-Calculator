# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:42:40 2019

@uthor: ric
"""

import tkinter as tk
from tkinter import ttk
import tkcalendar
#import Calendar
# import datetime
# import TKcal.Calendar import TKcal.DateEntry
#from tkcalendar import calendar_,  dateentry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


def example1():
    def print_sel():
        print(TKcal.calendar_.selection_get())
        cal.see(datetime.date(year=2016, month=2, day=5))

    top = tk.Toplevel(root)

    import datetime
    today = datetime.date.today()

    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(days=5)
    print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def example2():

    top = tk.Toplevel(root)

    cal = TKcal.calendar_(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()


def example3():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                          foreground='white', borderwidth=2, year=2010)
    cal.pack(padx=10, pady=10)


root = tk.Tk()
ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

root.mainloop()
