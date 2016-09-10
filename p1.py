from __future__ import division
import numpy
import os


with open('data_corrected/classification task/autos/train_docs/autos_file0.txt','r') as myfile:
    file = myfile.read()

tokens = file.split()
beginIndex = tokens.index('Subject')+2
tokens = tokens[beginIndex:]
tokens = [item for item in tokens if '@' not in item]
tokens = [item for item in tokens if item is not '>']


#Building Dictionary
dictionary = {}


"""for i in range(0,300):
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
              dictionary[tokens[index]] = dictionary[tokens[index]]+1"""

for index in range(len(tokens)):
    if tokens[index] not in dictionary:
        dictionary.update({tokens[index]:1})
    else:
        dictionary[tokens[index]] = dictionary[tokens[index]]+1
    

#Random Generator

values = dictionary.values()
valSum = sum(dictionary.values())
prob = [x / valSum for x in values]

random1 = numpy.random.choice(dictionary.keys(), p = prob)
random2 = numpy.random.choice(dictionary.keys(), p = prob)
random3 = numpy.random.choice(dictionary.keys(), p = prob)

#Bigram
dictionary2 = {}
for index in range(len(tokens)-1):
    if tokens[index] not in dictionary2:
        dictionary2.update({tokens[index]:{tokens[index+1]:1}})
    else:
        if tokens[index+1] not in dictionary2[tokens[index]]:
            dictionary2[tokens[index]].update({tokens[index+1]:1})
        else:
            dictionary2[tokens[index]][tokens[index+1]] = dictionary2[tokens[index]][tokens[index+1]]+1

if tokens[len(tokens)-1] in dictionary2:
    dictionary2[tokens[len(tokens)-1]].update({'<s>':1})
else:
    dictionary2.update({tokens[len(tokens)-1]:{'<s>':1}})
    

def random_generator_unigram(dictonary):
    values = dictionary.values()
    valSum = sum(dictionary.values())
    prob = [x / valSum for x in values]
    random  = numpy.random.choice(dictionary.keys(), p = prob)
    sentence = ''
    while(random != '.'):
        sentence = sentence+' ' +random
        random = numpy.random.choice(dictionary.keys(), p = prob)
    
    return sentence + '.'

def random_generator_bigram(dictionary1, dictionary2):
    #generating the first word
    values = dictionary1.values()
    valSum = sum(dictionary1.values())
    prob = [x / valSum for x in values]
    first  = numpy.random.choice(dictionary1.keys(), p = prob)
    
    diction_prob = dictionary2
    for k in diction_prob:
        valSum = sum(diction_prob[k].values())
        for key,value in diction_prob[k].items():
            diction_prob[k][key] = value/valSum
    
    sentence = first
    random = numpy.random.choice(diction_prob[first].keys(), p = diction_prob[first].values())
    while(random != '.' and random != '<s>'):
        sentence = sentence+' ' +random
        random = numpy.random.choice(diction_prob[random].keys(), p = diction_prob[random].values())
    
    return sentence + '.'
    

