import csv
from textblob import TextBlob

politics = []
sport = []
entertainment = []

#print(s2)
with open('sport.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s1 = row['news']
        blob = TextBlob(s1)
        s2 = blob.words
        for word in s2:
            if word not in sport:
                sport.append(word)
#print(sport)

with open('politics.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s1 = row['news']
        blob = TextBlob(s1)
        s2 = blob.words
        for word in s2:
            if word not in politics:
                politics.append(word)

#print(politics)

with open('entertainment.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        s1 = row['news']
        blob = TextBlob(s1)
        s2 = blob.words
        for word in s2:
            if word not in entertainment:
                entertainment.append(word)

#print(entertainment)

       
