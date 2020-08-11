# coding=utf-8

import os
import numpy as np
import codecs
from math import *



input_path = "E:\\数据集\\ic_18\\icdar2018\\test\\gt"
save_path = "E:\\数据集\\ic_18\\icdar2018\\test\\revise_gt"
n=0
filelist = os.listdir(input_path)
for item in filelist:
     
    txt_path = os.path.join(input_path, item)
 
    f=open(txt_path, mode='r', encoding='utf-8')
    
    new_save_path = os.path.join(save_path, item)
    
    f1=open(new_save_path, mode='w', encoding='utf-8')
    lines = f.readlines()
    #print('lines',lines)

    
    for line in lines:
        line = line.rstrip()       
        #用来解决icdar2019数据集标签后面存在","问题。
        line = line.rstrip(",")
        
        
        #line = line.split(' ')
        line = line.split(',')
        word = line[-1]
        new_line = str(line[0])+',' + str(line[1])+','+str(line[6])+','+str(line[7])+','+str(line[4])+','+str(line[5])+','+str(line[2])+','+str(line[3])
        print('new_line',new_line)
 
        l = new_line+','+ word
        print('l',l)
        f1.write(l+'\n')   

            
    n+=1    
    print(n)
    
