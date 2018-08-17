#coding=utf-8
from tkinter import *
import difflib
import time
import os


def windows(self):
    window = Tk()
    window.title("PTE的write from dictionary练习")
    frame1 = Frame(windows)
    frame1.pack()
    label = Label(frame2,text = "输入句子")
    self.sentence = StringVar()
    entrysentence = Entry(frame1,textvarible = self.sentence)

def readfromfile(name):
    memlist = {}
    i = 1
    	
    for line in open(name):
        memlist[i] = line
        i=i+1
    return memlist

def dictout(memlist,i):
    sentence = memlist[i]
    sentence = sentence[:-1]
    return sentence

def writetofile(sen,i,filename):
	fo = open(filename,"a")
	fo.write(str(i)+".      "+sen+"\n")
	fo.close

	
def writetofilecorrection(dictsen,i,filename):
	fo = open(filename,"a")
	fo.write(str(i)+".corr  "+dictsen+"\n")
	fo.close

def readfromtype(i):
    sen = input("this is the "+str(i) + "th sentence.")
    return sen

def matching(sen, dictsen):
    d = difflib.Differ()
    diff = d.compare(sen.splitlines(),dictsen.splitlines())
    return diff
		
def musicplay(i,floder):
    musicname = floder+str(i)+".m4a"
    os.system(musicname)
    return 6

print("PTE WDF练习运行")
option = input("请选择WDF的题库，1:2018年7月题库；2:2018年3月题库；3;2017年10月题库；4:2017年5月题库")
if option =="1":
    nameofaudiotext = "audiotext\\187.txt"
    nameofaudiofolder = "187\\"
    nameofwritingfile = "pra\\187.txt"
elif option =="2":
    nameofaudiotext = "audiotext\\183.txt"
    nameofaudiofolder = "183\\"
    nameofwritingfile = "pra\\183.txt"
elif option =="3":
    nameofaudiotext = "audiotext\\1710.txt"
    nameofaudiofolder = "1710\\"
    nameofwritingfile = "pra\\1710.txt"
elif option =="4":
    nameofaudiotext = "audiotext\\175.txt"
    nameofaudiofolder = "175\\"
    nameofwritingfile = "pra\\175.txt"

dictinfo = readfromfile(nameofaudiotext)
dictlen =  len(dictinfo)
i=1
for i in range(1,dictlen+1):
    time.sleep(musicplay(i,nameofaudiofolder))
    sen = readfromtype(i)
    writetofile(sen,i,nameofwritingfile)
    
    dictsen = dictout(dictinfo,i)
    writetofilecorrection(dictsen,i,nameofwritingfile)
    diff = matching(sen,dictsen)
    print("this is the matching result")
    print(sen)
    print("\n".join(list(diff)))
    time.sleep(2)
    print("let move to next question")
print("This type Question has finished.")

