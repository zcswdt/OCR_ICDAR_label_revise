import json
import numpy as np
import operator
#正则表达式库
import re
import cv2
import os
import numpy as np

root_path = './'
_indexes = sorted([f.split('.')[0]
                   for f in os.listdir(os.path.join(root_path, 'train_rename_totaltext_labels_sqfree'))])
for index in _indexes:
  print('Processing: ' + index)
  anno_file = os.path.join(root_path, 'train_rename_totaltext_labels_sqfree/') + index + '.txt'
  with open(anno_file,'r+') as f:
      #lines是每个文件中包含的内容
      lines = [line for line in f.readlines() if line.strip()]
      single_list = []
      all_list = []
      for i, line in enumerate(lines):
        #if i == 0:
          #continue
        #parts是每一行包含的内容
        parts = line.strip().split(',')
        xy_list = []
        for a, part in enumerate(parts):
            if a > 1:
              break
            piece = part.strip().split(',')
            numberlist = re.findall(r'\d+',piece[0])
            xy_list.extend(numberlist)
            
        length = len(xy_list)
        n = int(length / 2)
        x_list = xy_list[:n]
        y_list = xy_list[n:]
        single_list = [None]*(len(x_list)+len(y_list))
        single_list[::2] = x_list
        single_list[1::2] = y_list
        all_list.append(single_list)
        
  with open(anno_file,'w') as w:
      for all_list_piece in all_list:
        for string in all_list_piece:
          w.write(string)
          w.write(',')
        w.write('\n')