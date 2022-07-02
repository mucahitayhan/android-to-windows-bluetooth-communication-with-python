import json
import os
import cv2
import numpy as np
import shutil
import time

liste=[]
tarama=os.scandir('/home/aesk/Desktop/bagdata2')
for jpgler in tarama: 
    liste.append(jpgler.name)
liste.sort()

file1=open("/home/aesk/Desktop/1/1.yaml","w")
file2=open("/home/aesk/Desktop/2/2.yaml","w")
file3=open("/home/aesk/Desktop/3/3.yaml","w")
file4=open("/home/aesk/Desktop/4/4.yaml","w")
file5=open("/home/aesk/Desktop/5/5.yaml","w")
file6=open("/home/aesk/Desktop/6/6.yaml","w")


a=0
b=1
c=2
d=3
e=4
f=5

for k in range(105):
    file1.write("- url: items/1/{}\n  videoName: 1\n".format(liste[a]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[a]),"/home/aesk/Desktop/1/%s"%(liste[a]))
    a=a+6

for k in range(105):
    file2.write("- url: items/2/{}\n  videoName: 2\n".format(liste[b]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[b]),"/home/aesk/Desktop/2/%s"%(liste[b]))
    b=b+6

for k in range(105):
    file3.write("- url: items/3/{}\n  videoName: 3\n".format(liste[c]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[c]),"/home/aesk/Desktop/3/%s"%(liste[c]))
    c=c+6

for k in range(105):
    file3.write("- url: items/4/{}\n  videoName: 4\n".format(liste[c]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[c]),"/home/aesk/Desktop/4/%s"%(liste[c]))
    d=d+6

for k in range(105):
    file3.write("- url: items/5/{}\n  videoName: 5\n".format(liste[c]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[c]),"/home/aesk/Desktop/5/%s"%(liste[c]))
    e=e+6

for k in range(105):
    file3.write("- url: items/6/{}\n  videoName: 6\n".format(liste[c]))
    shutil.copy("/home/aesk/Desktop/bagdata/%s"%(liste[c]),"/home/aesk/Desktop/6/%s"%(liste[c]))
    f=f+6