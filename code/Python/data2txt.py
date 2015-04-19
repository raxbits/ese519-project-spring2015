# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:24:16 2015

@author: Jared
"""

import struct
import numpy as np
import pyqtgraph as pg
from pylab import *
import time

################################MOCK REAL TIME DATA###########################
#load up the MOCK data
labels = np.loadtxt('C:\Users\Jared\Dropbox\DEAPdatasets\Preprocessed_csv\s01Labels.csv',delimiter=',')
#data = np.loadtxt('C:\Users\Jared\Dropbox\DEAPdatasets\Preprocessed_csv\s01Datav2.csv',delimiter=',',usecols=range(1,8064*20),skiprows=0)
data = np.loadtxt('C:\Users\Jared\Dropbox\DEAPdatasets\Preprocessed_csv\s01Datav2.csv',delimiter=',')

def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

#init the txt for data in
#filename = "data.txt";
#target = open(filename, 'w')
#target.truncate()

#binary file
target =open('binaryFoo','wb')
target.truncate();

track = [];
for i in range(2000):
    x = struct.pack('f',data[1,i])
    track.append(struct.pack('f',data[1,i]))
    target.write(x)
    
    #target.write(binary(data[1,i]))
    #target.write("\n")
    print(i);
    
print "Fin"
target.close();