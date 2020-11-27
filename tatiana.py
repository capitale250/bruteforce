from itertools import product

print("mobile money by mtn passwords:")
fp=open("ncee.txt","w+")
chrs="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def count():
    for i in range(3,5):
        for xs in product(chrs, repeat=i):
          yield xs
def convertTuple(tup):
    str =  ''.join(tup)
    return str
for i in count():
    str = convertTuple(i)
    fp.write(""+str+"\n")

    print(str)
fp.close()
print()
print("We are computing all possible momo password in single line of code:")
print(list(product([1, 2,3,4,5,6,7,8,9,0],repeat=5 )))
print()

['1', '2','3','4','5','6','7','8','9','0']
print("We are computing all possible password in alphabets in range of 2 and 5 characters:")
try:
 for i in range(3,4):
  print(list(product(chrs,repeat=i)))
finally:
 print("ERROR FOUND")


import tkinter as tk
import mysql.connector
from datetime import datetime
from tkinter import *
now = datetime.now()

print("now =", now)




# dd/mm/YY H:M:S
d_string = now.strftime(" %H:%M:%S")
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print("date and time =", dt_string,d_string)






root = tk.Tk()
root.geometry('700x450')
root.title("@capitale library")
background_image = tk.PhotoImage(file='create_thumb.png')
background_label = tk.Label(root, image=background_image).pack(side="right")
def insert():



    top = Toplevel()
    top.title('Python')
    background_image = top.PhotoImage(file='create_thumb.png')
    background_label = top.Label(root, image=background_image).pack(side="right")
    top.mainloop()

buttoncal = tk.Button(root,text="Submit",command=insert).place(x=30,y=370)

root.mainloop()
  
import tkinter as tk
from functools import partial
import mysql.connector
from datetime import datetime
from PIL import Image
from tkinter import *
import pandas as pd
import mysql