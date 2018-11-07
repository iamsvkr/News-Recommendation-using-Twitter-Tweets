import csv
from textblob import TextBlob

x = set([])
business = []
entertainment = []
politics = []
sport = []
tech = []
with open('entertainment.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s = row['news']
        #print(s)
        blob = TextBlob(s)
        s1 = blob.words
        for word in s1:
            x.add(word)
        

#print(x)
file = open('entertainment1.txt','w')
for y in x:
    #file.writelines(y)
    #print(y)
    file.write(y)
    file.write('\n')
file.close()

with open('sport.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s = row['news']
        #print(s)
        blob = TextBlob(s)
        s1 = blob.words
        for word in s1:
            x.add(word)
        

#print(x)
file = open('sport1.txt','w')
for y in x:
    #file.writelines(y)
    #print(y)
    file.write(y)
    file.write('\n')
file.close()

with open('politics.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s = row['news']
        #print(s)
        blob = TextBlob(s)
        s1 = blob.words
        for word in s1:
            x.add(word)
        

#print(x)
file = open('politics1.txt','w')
for y in x:
    #file.writelines(y)
    #print(y)
    file.write(y)
    file.write('\n')
file.close()
