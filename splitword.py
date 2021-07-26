import os
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words
file=open("unique_sorted_words_in_all_words_20200604-133955.txt")
lines=file.read()
word=get_words(lines)
q=['ஃ','அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ',
       '௧','௨','௩','௪','௫','௬','௭','௮','௯','௰','௱','௲','ஶ','௦','க',        'ச','ஞ','ட','ண','த','ந','ப','ம','ய','ர','ல','வ','ழ',
'ள','ற','ன','ஹ','ஜ','ஷ','ஸ']
s=[]
for each in word:
    s.append(get_letters_length(each))
a=set(s)


def folder(value):
    dire="len_"+str(value)
    pardir="/home/abirami/Music/findfolder"
    path=os.path.join(pardir,dire)
    os.mkdir(path)
    return path
    

def txtfile(filename,length):
    m=[]
    y=[]
    for each in word:
       if get_letters_length(each)==length and each[0] in q:
          y.append(each)
          m.append(each[0])

    b=set(m)

    for x in b:
        file1=open(os.path.join(filename,str(x)+'.txt'),"w")
        for words in y:
            if words.startswith(x):
               file1.writelines("%s\n"%words)
               

for i in a:
    result=folder(i)
    txtfile(result,i)
