# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:18:08 2019

@author: ric
"""
from tkinter import *
import sys
import pickle
import tkinter

def makeInputMenu(mbar):
    InputBtn = Menubutton(mbar, text='Input', underline=0, command=SubsidyCalculorInput())
    InputBtn.pack(side=LEFT, padx="2m")
    InputBtn.menu = Menu(InputBtn)
    InputBtn['menu'] = InputBtn.menu
    return InputBtn

def makeOutputMenu(mbar):
    OutputBtn = Menubutton(mbar, text='Output', underline=0, command=SubsidyCalculorOutput())
    OutputBtn.pack(side=LEFT, padx="2m")
    OutputBtn.menu = Menu(OutputBtn)
    OutputBtn['menu'] = OutputBtn.menu
    return OutputBtn

def makePrintMenu(mbar):
    PrintBtn = Menubutton(mbar, text='Print', underline=0, command=Print())
    PrintBtn.pack(side=LEFT, padx="2m")
    PrintBtn.menu = Menu(PrintBtn)
    PrintBtn['menu'] = PrintBtn.menu
    return PrintBtn

def makeSettingMenu(mbar):
    SettingBtn = Menubutton(mbar, text='Setting', underline=0)
    SettingBtn.pack(side=LEFT, padx="2m")
    SettingBtn.menu = Menu(SettingBtn)
    SettingBtn.menu.add_command(label="Member", underline=0, command=Member())
    SettingBtn.menu.add_command(label='Unit', underline=0, command=Unit())
    SettingBtn.menu.add_command(label='Renscale', underline=0, command=RentScale())
    SettingBtn.menu.add_command(label='Codes', underline=0, command=Code())
    SettingBtn['menu'] = SettingBtn.menu
    return SettingBtn

def makeHelpMenu(mbar):
    HelpBtn = Menubutton(mbar,text='Help', underline=0)
    HelpBtn.pack(side=LEFT, padx="2m")
    HelpBtn.menu = Menu(HelpBtn)
    HelpBtn.menu.add_command(label="Overview", underline=0, command=Overview()) 
    HelpBtn.menu.add_command(label='Input', underline=0, command=Input())
    HelpBtn.menu.add_command(label='Output', underline=0, command=Output())
    HelpBtn.menu.add_command(label='Codes', underline=0, command=Codes())
    HelpBtn['menu'] = HelpBtn.menu
    return HelpBtn

def makeExitMenu(mbar):
    ExitBtn = Menubutton(mbar,text='Exit', underline=0, command=root.quit
#    ExitBtn.pack(side=LEFT, padx="2m")
#    ExitBtn.menu = Menu(ExitBtn)
#    ExitBtn['menu'] = ExitBtn.menu
    return ExitBtn

#def quit():
#    import sys 
#    systemexit() 
               
def SubsidyCalculorInput():
    root.title("Subsidy Calculor Input")
    lbl=Label(root,text="in SubsidyCalculorInput ")
    lbl.pack()

def SubsidyCalculorOutput():
    root.title("Subsidy Calculor Output")
    lbl=Label(root,text="in SubsidyCalculorOutput ")
    lbl.pack()

def Print():
    root.title("Code Management")
    lbl=Label(root,text="in Print")
    lbl.pack()

def Setting():
    root.title("Code Management")
    lbl=Label(root,text="in Setting ")
    lbl.pack()

def Help():
    root.title("Help")
    lbl=Label(root,text="in Help ")
    lbl.pack()
 
def Exit():
    root.title("Exit")
    lbl=Label(root,text="in Exit ")
    lbl.pack()
   
def Member():
    root.title("Member")
    lbl=Label(root,text="in Member ")
    lbl.pack()
   
def Unit():
    root.title("Unit")
    lbl=Label(root,text="in Unit ")
    lbl.pack()
   
def RentScale():
    root.title("RentScale")
    lbl=Label(root,text="in RentScale ")
    lbl.pack()
   
def Code():
    root.title("Code")
    lbl=Label(root,text="in Code ")
    lbl.pack()
   
def Overview():
    root.title("Overview")
    lbl=Label(root,text="in Overview ")
    lbl.pack()

def Input():
    root.title("Input")
    lbl=Label(root,text="in Input ")
    lbl.pack()

def Output():
    root.title("Output")
    lbl=Label(root,text="in Output ")
    lbl.pack()

def Codes():      
    root.title("Codes")
    lbl=Label(root,text="in Codes ")
    lbl.pack()
    
def displaymenu(mbar):
    InputBtn = makeInputMenu(mbar)
    OutputBtn = makeOutputMenu(mbar)
    PrintBtn = makePrintMenu(mbar)
    SettingBtn = makeSettingMenu(mbar)
    HelpBtn = makeHelpMenu(mbar)
    ExitBtn = makeExitMenu(mbar)
    #NoMenu =SubsidyCalcultor.makeDisabledMenu()
#    root.tk_menuBar(InputBtn, OutputBtn, PrintBtn, SettingBtn,HelpBtn, Exit)

root = Tk()
root.title("Subsidy Calculor")
mBar = Frame(root)
mBar.pack(fill=X)
displaymenu(mBar)
root.mainloop()
