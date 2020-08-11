# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys,os



input_path = "E:\\数据集\\ic_18\\icdar2018\\test\\img"
txt_path = "E:\\数据集\\ic_18\\icdar2018\\test\\gt"


fileList=os.listdir(input_path)
n=0
for i in fileList: 

    new = i.split('.')[-1]
    new_s = '.'+ new    
    print('new_s',new_s)

    fo = i.split('.')[:-1]
    print('fo',fo)
    fo_1 = '.'.join(fo)    
    
    img_path = os.path.join(input_path,i)
    dst = os.path.join(os.path.abspath(input_path), 'tb_' + str(n) + new_s)
    print('dst',dst)
    os.rename(img_path, dst)
    
     "gt_%s.txt" % os.path.splitext(imagename)[0]
    
    txt_name = fo_1+'.txt'
    
    #txt_name = i.replace(new_s, ".txt")
    print('txt_name',txt_name)
    new_txt_path = os.path.join(txt_path, txt_name)
    
    dst1 = os.path.join(os.path.abspath(txt_path), 'tb_' + str(n) + '.txt')
    os.rename(new_txt_path, dst1)
    
    n+=1
    print('n',n)
    
    
    


        
    