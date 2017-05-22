import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import random


file = open('cleandata.txt', 'r')

tweets = file.read().splitlines()



text= []
for tweet in tweets:
    text.append(word_tokenize(tweet))

#print nltk.pos_tag(text[0])
tagged_text = []
for tweet in text:
    tagged_text.append(nltk.pos_tag(tweet))


clean_tagged_text = []


for tweet in tagged_text:
    for x in tweet:
        clean_tagged_text.append(x)

listofverbs = []
for word,pos in clean_tagged_text:
    if pos == 'VBN' or pos == 'VBD':
        listofverbs.append(word)
listofin = []
for word, pos in clean_tagged_text:
    if pos== 'IN':
        listofin.append(word)
listofvbg= []
for word, pos in clean_tagged_text:
    if pos=='VBG':
        listofvbg.append(word)
listofnouns = []
for word, pos in clean_tagged_text:
    if pos =='NN' or pos =='NNS' or pos == 'NNP':
        listofnouns.append(word)

random1 = random.randint(0,len(listofverbs)-1)
random2 = random.randint(0,len(listofin)-1)
random3 = random.randint(0,len(listofvbg)-1)
random4 =random.randint(0, len(listofnouns)-1)



for x in listofnouns:
    if x =='man':
        listofnouns.remove('man')
listofnouns.append('man')

#print "Florida man" +" "+listofverbs[random1]+" "+listofin[random2]+" "+listofvbg[random3]+" "+listofnouns[random4]+'.'
setofverbs =set(listofverbs)
print len(setofverbs)
for x in setofverbs:
    if x=='seen' or x =='slept' or x =='was':
        print "buz"
