from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
import numpy


with open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r') as myfile:
    file = myfile.read()
#file = open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r')



sentence = "At eight o'clock on Thursday morning Arthur didn't feel very very good. on Monday morning Arthur feels better"
tokens = nltk.word_tokenize(sentence)


import nltk, re, pprint
from nltk import word_tokenize

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very very good . on Monday morning Arthur feels better"
#tokens = nltk.word_tokenize(file)
tokens = file.split()
beginIndex = tokens.index('Subject')+2
tokens = tokens[beginIndex:]
tokens = [item for item in tokens if '@' not in item]
tokens = [item for item in tokens if item is not '>']


#Building Dictionary
dictionary = {}


for i in range(0,300):
    if i == 171:
        pass
    else:
       filename = 'data_corrected/classification task/autos/train_docs/autos_file'+str(i)+'.txt'
       with open(filename,'r') as myfile:
           file = myfile.read()
       tokens = nltk.word_tokenize(file)
    
       for index in range(len(tokens)):
          if tokens[index] not in dictionary:
              dictionary.update({tokens[index]:1})
          else:
              dictionary[tokens[index]] = dictionary[tokens[index]]+1

"""with open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r') as myfile:
    file = myfile.read()
#file = open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r')

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very very good. on Monday morning Arthur feels better"
tokens = nltk.word_tokenize(file)
for index in range(len(tokens)):
    if tokens[index] not in dictionary:
        dictionary.update({tokens[index]:1})
    else:
        dictionary[tokens[index]] = dictionary[tokens[index]]+1"""
    

#Random Generator
test = numpy.random.choice(["a","b","c"], p=[0.2,0.3,0.5])
values = dictionary.values()
valSum = sum(dictionary.values())
prob = [x / valSum for x in values]

random1 = numpy.random.choice(dictionary.keys(), p = prob)
random2 = numpy.random.choice(dictionary.keys(), p = prob)
random3 = numpy.random.choice(dictionary.keys(), p = prob)





##re.replace(orinical, re_for_email,"")



## x 1 = text
x2 = x.split()
x3 = [a for a in x2 if '@' not in a]   '[at]'

