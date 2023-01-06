# Employee Portal all
# TODO interface they can log into to see payroll and employment data
# TODO employee portal for time clock data input
# TODO tech hrs input
# TODO tech hr input cannot exceed value of pre recorded hrs + input > approved hrs
# TODO a standard practice that can be done by any manager.

# test to see changes

import tkinter.ttk
from tkinter import *

# Start of Code and Main Window

Login_Gui = Tk()
Login_Gui.option_add('*Font', '35')
Login_Gui.geometry('700x120')
Login_Gui.title("Total MINI & BMW Tech Hours Portal")

# second Frame
Login_Gui_Header = tkinter.Frame(Login_Gui)
Login_Gui_Header.grid(row=0, column=0, padx=10, pady=10)

emp_name = tkinter.Label(Login_Gui_Header, text="Tech Name", padx=30, pady=5)
emp_name.grid(row=0, column=0)

emp_name_entry = tkinter.ttk.Combobox(Login_Gui_Header, values=["Ryan Bowers", "Austin Calvert", "Anthony Cucaz",
                                                                "Chip Myers", ])
emp_name_entry.grid(row= 0, column= 1)

pword = tkinter.Label(Login_Gui_Header, text="Password")
pword.grid(row=1, column=0)

password_entry = tkinter.Entry(Login_Gui_Header)
password_entry.grid(row=1, column=1)

# good/\

tkinter.Button(Login_Gui_Header, text="Log in", background="grey", foreground='white',
               font="rockwell").grid(column=1, row=3, pady=10, padx=10)

# Employee Data Entry

# for GUI
# Window Frames


# labels
# password
# for GUI
Login_Gui.mainloop()
