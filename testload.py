# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:04:58 2019

@author: ric
"""

from tkinter import *
from tkinter import messagebox 
import ast
#import Tkinter
#
#tkbase = Tk()
class VarList():
    def __init__(self,action,varlist):
       self.action = action
       self.varlist = varlist
       if self.action == "save":
            self.Save()            
       elif self.action == "load":
            self.Load()
       else:           
           messagebox.showerror("actiom", "action is not valid") 

    def Save(self):
        self.whip = self.varlist 
        target = open('data.txt', 'a')
        target.write(str(self.whip))
        
    def BuildVarList(self):
        pass
        
    def ParseVarList(self,var,value):
            self.whip[var] = self.whip[value]     
        
    def Load(self):
        with open('data.txt', 'r') as f:
            self.varliststr = f.read()
            print(f.read())
            return self.varliststr
#            outdict = ast.literal_eval(s)
#            for var, value in outdict.items():
#                self.ParseVarList(var,value)
#            print(self.whip[var] = self.whip[value])
varlist = {}       
#varlist = dict({"members":members,"ratescale":ratescale})
loadvar = VarList("load",varlist)
varliststr = loadvar.Load()
