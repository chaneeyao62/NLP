a = 101
with open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r') as myfile:
    file = myfile.read()
#file = open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r')

import nltk, re, pprint
from nltk import word_tokenize
sentence = "At eight o'clock on Thursday morning Arthur didn't feel very very good. on Monday morning Arthur feels better"
tokens = nltk.word_tokenize(file)

dictionary = {}

for index in range(len(tokens)):
    if tokens[index] not in dictionary:
        dictionary.update({tokens[index]:1})
    else:
        dictionary[tokens[index]] = dictionary[tokens[index]]+1
    
    #ggggg
    