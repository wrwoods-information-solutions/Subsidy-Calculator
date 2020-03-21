# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:25:05 2019

@author: ric
"""

import pickle
pickleload = open("SCData.pickle", "rb")
varname = pickle.load(pickleload)
members = varname["members"]
print(varname['byunitlist'])
