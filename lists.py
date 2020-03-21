# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:47:36 2019

@author: ric
"""
import SCData
# sentence_list = ["my", "name", "is", "George"]
# sentence_string = " ".join(sentence_list)
# print(sentence_string)
for n in SCData.members:
#    if len(SCData.byunitlist) == 0:
    SCData.byunitlist.extend(str(SCData.members[n]['UNIT']))
print(SCData.byunitlist)
#    else:
#        SCData.byunitlist = ",".join([str(SCData.members[n]['UNIT'])])
