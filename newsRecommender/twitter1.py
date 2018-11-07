import tweepy
import csv
from textblob import TextBlob
#from bs4 import BeautifulSoup as soup
#from urllib.request import urlopen
import tkinter as tk

root = tk.Tk()

consumer_key = 'hwPwR5mW3S9zKmZFrgyqlium5'
consumer_secret = 'yKMqhGa0McTg90KnEZi3rtKuZRIqeoX68UQtN3fhA88jNfmZ0W'
access_token = '821758363029663745-kd4dTNwOul2E509DPLe53a9Z5Ypi1pa'
access_token_secret = 'W5fUF7UzGMv1s4eVEc5qwT3yo087KbSW1URmtV0SEtJib'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def biggest(a, y, z):
    if a>=y and a>=z:
        return a
    elif y>=a and y>=z:
        return y
    else:
        return z

def get_tags(tweets):
    sport=0
    entertainment = 0
    politics = 0
    tags = []
    for tweet in tweets:
        blob = TextBlob(tweet)
        s2 = blob.words
        #print(s2)
        with open('sport1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['sword']
                if s in s2:
                    sport = sport + 1
        #print(sport)

        with open('politics1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['pword']
                if s in s2:
                    politics = politics + 1

        #print(politics)

        with open('entertainment1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['eword']
                if s in s2:
                    entertainment = entertainment + 1

        #print(entertainment)

        u = biggest(sport,politics, entertainment)
        #print(u)
        if sport==u:
            #print("sport")
            tags.append("sport")
        elif politics==u:
            tags.append("politics")
        else:
            tags.append("entertainment")
            #print("entertainment")
    return tags

def get_tag(news):
    sport=0
    entertainment = 0
    politics = 0
    for tweet in tweets:
        blob = TextBlob(tweet)
        s2 = blob.words
        #print(s2)
        with open('sport1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['sword']
                if s in s2:
                    sport = sport + 1
        #print(sport)

        with open('politics1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['pword']
                if s in s2:
                    politics = politics + 1

        #print(politics)

        with open('entertainment1.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                s = row['eword']
                if s in s2:
                    entertainment = entertainment + 1

        #print(entertainment)

        u = biggest(sport,politics, entertainment)
        #print(u)
        if sport==u:
            #print("sport")
            tag = "sport"
        elif politics==u:
            tag = "politics"
        else:
            tag = "entertainment"
            #print("entertainment")
    return tag

def get_tweets(username):
    text = []
    tweets = api.user_timeline(screen_name = username, count = 10, include_rts = True)
    for status in tweets:
        text.append(status.text)
    return text

if __name__ == '__main__':
    tweets = []
    s = input("Enter the twitter handle : ")
    tweets = get_tweets(s)
    tags = []
    tags = get_tags(tweets)
    print(tags)
#    for tag in tags:
#        for news in news_list:
#            tg = get_tag(news.title.text)
#            if tg == tag:
#                print("news : " + news.title.text)
 #               del news_list[0]
  #              break
    sportNews = []
    politicsNews = []
    entertainmentNews = []
    with open('sportsNews.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sportNews.append(row['news'])
            
    with open('politicsNews.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            politicsNews.append(row['news'])
    
    with open('entertainmentNews.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entertainmentNews.append(row['news'])
            
    tk.Label(root, text = s, fg = "black", bg = "white",font = "Helvetica 16 bold italic").pack()
    
    for tag in tags:
        if tag == "sport":
            #print(sportNews[0])
            tk.Label(root, text= "Sport : " + sportNews[0], fg = "white", bg = "blue",font = "Helvetica 16 bold italic").pack()

            del sportNews[0]
        
        if tag == "politics":
            #print(politicsNews[0])
            tk.Label(root, text= "Politics : " + politicsNews[0], fg = "white", bg = "red",font = "Helvetica 16 bold italic").pack()
            del politicsNews[0]
        
        if tag == "entertainment":
            #print(entertainmentNews[0])
            tk.Label(root, text= "Entertainment : " + entertainmentNews[0], fg = "white", bg = "green",font = "Helvetica 16 bold italic").pack()
            del entertainmentNews[0]
    
    root.mainloop()
    #msdhoni
    #iamsrk
    #iamVkohli
    #sherryontopp
    #KapilSharmaK9