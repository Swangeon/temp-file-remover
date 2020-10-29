#! python3

#Import the modules I need
import os
import shutil
from datetime import *
from tkinter import *


#The function I need to determine what wasn't deleted and the delete instructions
def rmdirs(path):
    for filename in os.listdir():
        shutil.rmtree(str(path), ignore_errors = True)

def logwriter():
    os.chdir(r'C:\Users\Swangeon\Desktop\Coding Stuff\Python\temp file eraser project')
    logfile = open('Templog.txt', 'a+')
    logfile.write('\n' + '-' * 50)
    for filename in os.listdir('C:\\Users\\Swangeon\\AppData\\Local\\Temp'):
        logfile.write("\nDate: " + str(datetime.now()) + "\n\t'%s' was not deleted"% filename)
    logfile.close()

def update():
    lb1.delete(0, END)
    for item in list(os.listdir('C:\\Users\\Swangeon\\AppData\\Local\\Temp')):
        lb1.insert(END, item)

#TEMP directory delete final function   
def tempdelete():
    rmdirs('C:\\Users\\Swangeon\\AppData\\Local\\Temp')
    logwriter()
    update()

os.chdir('C:\\Users\\Swangeon\\AppData\\Local\\Temp')

templist = os.listdir()

w = Tk()

w.title('Temp File Eraser')

L1 = Label(w, text = 'Now in ' + os.getcwd())
L1.pack()
#L1.grid(row = 0, column = 0, rowspan = 1)

lb1 = Listbox(w, width = 36, height = 12)
lb1.insert(END, *templist)
lb1.pack(side = LEFT)
#lb1.grid(row = 1, column = 0)

sb1 = Scrollbar(w)
sb1.pack(side = LEFT, fill = Y)
#sb1.grid(row = 1, column = 1, rowspan =6)

sb2 = Scrollbar(w)
sb2.pack(side = BOTTOM, fill = X)
#sb2.grid(row = 2, column = 0, padx = 10)

lb1.configure(yscrollcommand = sb1.set, xscrollcommand = sb2.set)
sb1.configure(command = lb1.yview)
sb2.configure(command = lb1.xview)

b1 = Button(w, text = 'Delete', command = tempdelete)
b1.pack(side = TOP, pady = 5)
b2 = Button(w, text = 'Quit', command = quit)
b2.pack(side = TOP)

w.mainloop()
