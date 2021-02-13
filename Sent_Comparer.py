#author ESHAN K KAUSHAL - 17103116
#The Code below finds and compare the texts between 2 files
#Just change the text doc in the file = open() line
#problem: same words get repeated even after removing them from the list
import nltk
import threading
import logging
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk import tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from langdetect import detect
from nltk.stem import PorterStemmer
ps = PorterStemmer()

special = [".", ",", "'"]
exit_exit = ["Bye", "bye", "Goodbye", "goodbye", "talk to you later",
                 "bye-bye", "bye bye", "byebye", "ByeBye",
                     "TTYL", "BB", "B", "GG", "b", "gg", "exit", "Exit", "EXIT", "N", "NO", "n", "no"]

stop_words = set(stopwords.words("english"))
#nltk.download('state_union')
#nltk.download('averaged_perceptron_tagger')

#print(sample_txt.readable())    
#print(sample_txt.read())
#no of lines



file = open("V8_Engines.txt", "r")



file2 = open("V10_Engines.txt", "r")




sc = 0
counter = 0
sample_txt = file.read()
sample_txt2 = file2.read()
lines  = sample_txt.split("\n")
for i in lines:
    if i:
        counter += 1
print("The number of lines in the document is:")
print(counter)

words = sample_txt.split()
print("The number of words in the document is:")
print(len(words))

words2 = sample_txt2.split()
print("The number of words in the 2nd document is:")
print(len(words2))

print("The language of the document is:")
print(detect(sample_txt))
print("\n")

fs1 = []
fs2 = []
fs3 = []
#for i in word_tokenize(sample_txt):
#    if ((i not in stop_words) and (i not in special)):
#        fs1.append(i)
#for i in word_tokenize(sample_txt2):
#    if ((i not in stop_words) and (i not in special)):
#        fs2.append(i)

#for i in fs1:
#    #print("Match:")
#    for j in fs2:
#        if (i==j):
#            
#            #print("Match:")
#            fs3.append(i)
#            fs2.remove(j)
#            #print(i)
#            sc += 1
#    fs1.remove(i)    
#for i in fs3:
#    print(i)
#print("Total Count:")
#print(sc)
sent_1 = sent_tokenize(sample_txt)
sent_2 = sent_tokenize(sample_txt2)
sent_3 = []
#print(sent_1)
#print(sent_2)
for i in sent_1:
    for j in sent_2:
        if (i==j):
            sent_3.append(i)
            sent_2.remove(j)
            sc +=1
    sent_1.remove(i)
for i in sent_3:
    print(i)
print("No. of Matched sentences:")
print(sc)
            



