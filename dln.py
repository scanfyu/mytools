# -*- coding: utf-8 -*-
'''
inputname = '/in.txt'
outputname = '/out.txt'

def remove(inputname):
    with open(inputname) as f:
        print f
        reader = 
    
    content = open(txt_filename,'w')
    for each in content.readlines():
        each = str(each).replace("\n"," ")
        print each
    content.write(each)
    content.close()
'''

#-*- coding=utf-8 -*-
#python3

content = open('E:\\GitHub\\mytools\\in.txt', 'rb')
each2 = ""
for each in content.readlines():
    each1 = str(each).replace("\\n"," ").replace("\\r", "").replace("b", "").replace("'", "")
    each2 = each2+each1
    #print each2
    print each1
content.close()
print (each2)
f = open('E:\\GitHub\\mytools\\out.txt', 'w')
f.writelines(each2)
f.close()
