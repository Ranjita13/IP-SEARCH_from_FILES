"""
Importing packages
"""
import os
import datetime
import re
from IPy import IP
import sys
import time
import numpy as np

"""
*********************************************************************************************************************
Checking argument line
"""
if (str(sys.argv[1])=='sample.log'):
    if (str(sys.argv[2])=='query'):
        print("the Order is correct")
else:
    print("Caution: The order or file is incorrect or check the file name.")
    exit()


"""
*********************************************************************************************************************
Parsing the sample.log
"""
IP_arr=[]
r1=re.compile('/.*.html')
r2=re.compile('200')
count=1
if (str(sys.argv[1])=='sample.log'):
       f  = open(sys.argv[1], "r")
       print (type(f))
       a=f.readlines()
       for lines in a:
            arr_l = lines.split(" ")
            if(time.strptime(arr_l[0],'%Y-%m-%d')):
                print()
            if(time.strptime(arr_l[1],'%H:%M:%S')):
                print()
            if (IP(arr_l[2])):
                print()
                IP_arr.append(arr_l[2])
            if(re.match(r1,arr_l[3])):
                print()
            if(re.match(r2,arr_l[4])):
                print("Everything is in format. Parsed Line: ",count)
            count=count+1
print("\nLoading IP addresses in memory.. ")

"""
*********************************************************************************************************************
Saving the IP address in temp location and loading it to the memory
"""
np.save('/tmp/123',IP_arr)
X=np.load('/tmp/123.npy')


"""
*********************************************************************************************************************
Opening query file and matching with the log-file's IP address
"""
ip_arr1=[]
if (str(sys.argv[2]) == 'query'):
       f  = open(sys.argv[2], "r")
       a1=f.readlines()
       print("\nPrinting output after match both files: ")
       for lines in a1:
           arr_l1 = lines.split("\n")
           if (arr_l1[0] in X):
               print("1")
           else:
               print("0")

"""
*********************************************************************************************************************
"""