# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:23:27 2020

@author: fatih cihan
"""
"""
Cdeki input.txt dosyasini okur output.txt dosyasini bilgisayardaki ayarlara göre belirlenen yere kaydeder.
"""
import operator
f=open("C:/input.txt","r")
allChar=f.read()
wordCount=dict()
nextWordCount=dict()
wordList = allChar.split()

for i in wordList:
    if i in wordCount:
        wordCount[i]+=1
    else:
        wordCount[i]=1
inp=input("input gir ")
inpList = inp.split()
for i in wordList:
    size=(len(inpList))
    if size>4:
       break
    if (inpList[size-1] == i):
        nextWord=wordList[wordList.index(i)+1]
        #print("nextwords--->",nextWord)
        wordList.remove(i)
        if nextWord in nextWordCount:
            nextWordCount[nextWord] +=1
        else:
            nextWordCount[nextWord]=1

if(len(nextWordCount)==0):
    result=("öneri yok")
else:
    result=(max(nextWordCount.items(), key=operator.itemgetter(1))[0])
fr=open("output.txt","w")
fr.write(result)
fr.close









 
 
 
    
    
    
    
    
    