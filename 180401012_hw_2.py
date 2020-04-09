# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:04:22 2020

@author: fatih cihan
"""
import operator
import sys
f=open(sys.argv[1] + "/input_hw_2.csv","r")
allChar=f.read()
wordList=allChar.split("\n")
monthFreq={}
size=len(wordList)-1

for i in range(0,size):    
    wl2=wordList[i].split(";")  
    wl3=wl2[3].split("-")    
    month=int(wl3[1])    
    if(month in monthFreq):
        monthFreq[month]=monthFreq[month]+1
    else:
        monthFreq[month]=1

sortedMonthFreq = sorted(monthFreq.items(), key=operator.itemgetter(1))
size2=len(sortedMonthFreq)

if(size2%2!=0):
    median=sortedMonthFreq[int(size2/2)][1]

else:
    median=sortedMonthFreq[size2/2-1][1]


psum=0
for i in sortedMonthFreq:
    psum+=i[1]
avr=psum/size2

fr=open(sys.argv[2] + "/180401012_hw_2_output.txt","w")
fr.write("Medyan: " + str(median) +"\n")
fr.write("Ortalama: " + str(avr) + "\n")
fr.close

























