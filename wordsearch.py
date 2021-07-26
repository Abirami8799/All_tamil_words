import os
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words
value = int(input("enter the word  "))
l=[]
for i in range(1,value+1):
    x=input(f'enter the letter {i} ')
    l.append(x)

n=''.join(map(str,l))

for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
    for name in dirs:
        if name == "len_"+str(value):
           a=os.path.join(root,name)
for root, dirs, files in os.walk(a):
    for val in files:
        if val.startswith(n[0]):
           b=os.path.join(root,val)
file1=open(b)
lines=file1.read()
word=get_words(lines)


r=get_letters_length(n)

for each in word:  
    m=get_letters(each)
    if each.startswith(l[0]) and each.endswith(l[value-1]):   
       y=[m.index(j) for i,j in zip(l,m) if i==j]
       if len(y)==r:
          print(''.join(map(str,m)))

 





                      
        


           
               
           






        


