#coding=utf-8
from tkinter import *
import difflib
import time
import os

## 文件名称和文件格式的规范化的代码因为涉及到有版权的文件，暂不提供，但是后期可能会放在无版权申诉条件的加密网盘中


##下面这个UI界面，暂时不考虑
def windows(self):
    window = Tk()
    window.title("PTE的write from dictionary练习")
    frame1 = Frame(windows)
    frame1.pack()
    label = Label(frame2,text = "输入句子")
    self.sentence = StringVar()
    entrysentence = Entry(frame1,textvarible = self.sentence)

##这个读取答案文件
def readfromfile():
    memlist = {}
    i = 1
	## 修改文件路径
    for line in open("read.txt"):
        memlist[i] = line
        i=i+1
    return memlist

def dictout(memlist,i):
    sentence = memlist[i]
    sentence = sentence[:-1]
    return sentence


def readfromtype(i):
    sen = input("this is the "+str(i) + "th sentence.")
    return sen

def matching(sen, dictsen):
    d = difflib.Differ()
    diff = d.compare(sen.splitlines(),dictsen.splitlines())
    return diff
	
## 文件名需要规范	
def musicplay(i):
    musicname = str(i)+".m4a"
    os.system(musicname)
    return 6

print("PTE WDF练习运行")
dictinfo = readfromfile()
dictlen =  len(dictinfo)
i=1
for i in range(1,dictlen+1):
    time.sleep(musicplay(i))
    sen = readfromtype(i)
    dictsen = dictout(dictinfo,i)
    diff = matching(sen,dictsen)
    print("this is the matching result")
    print(sen)
    print("\n".join(list(diff)))
    time.sleep(2)
    print("let move to next question")
    

