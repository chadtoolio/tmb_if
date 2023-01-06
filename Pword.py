
import tkinter.ttk

from tkinter import *

#Employee Log in GUI


#Start of Code and Main Window
Login_Gui = Tk()
Login_Gui.option_add('*Font' , '35')
Login_Gui.geometry('500x120')
Login_Gui.title("Total MINI & BMW Employee Portal")

#second Frame
Login_Gui_Header = tkinter.Frame(Login_Gui)
Login_Gui_Header.grid(row=0, column=0, padx= 10, pady= 10)

tech_name = tkinter.Label(Login_Gui_Header, text= "Tech Name", padx=30, pady=5)
tech_name.grid(row=0, column=0)



tech_name_entry = tkinter.ttk.Combobox(Login_Gui_Header, values=["Ryan Bowers", "Austin Calvert", "Anthony Cucaz", "Chip Myers"])
tech_name_entry.grid(row=0, column=1)

pword = tkinter.Label(Login_Gui_Header, text= "Password")
pword.grid(row=1, column=0)

password_entry = tkinter.Entry(Login_Gui_Header)
password_entry.grid(row=1, column=1)

tkinter.Button(Login_Gui_Header, text="Log in",
              background= "grey", foreground= 'white',
              font= ("rockwell")).grid(column=1, row=3, pady=10, padx=10)
#good/\



password_entry = tkinter.StringVar(value="toolman")

password_fr =tkinter.Label(Login_Gui_Header)
password_fr.grid(row=3, column=0)




Login_Gui.mainloop()


