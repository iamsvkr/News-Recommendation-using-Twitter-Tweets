import newspaper
import csv
from newspaper import Article

sportsNews = []
count = 0
paper = newspaper.build("https://www.news18.com/sports/", memoize_articles=False)
for article_name in paper.articles:
    #article_name = Article("https://www.breitbart.com/sports/", language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    #print(article_name.title)
    sportsNews.append(article_name.title)
    
    if(count>10):
        break
    count = count + 1

#print(sportNews)
with open('sportsNews.csv','w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['news'])
        for news in sportsNews:
            thewriter.writerow([news])


politicsNews = []
count = 0
paper = newspaper.build("https://www.indiatvnews.com/politics", memoize_articles=False)
for article_name in paper.articles:
    #article_name = Article("https://www.breitbart.com/sports/", language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    #print(article_name.title)
    politicsNews.append(article_name.title)
    
    if(count>10):
        break
    count = count + 1

with open('politicsNews.csv','w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['news'])
        for news in politicsNews:
            thewriter.writerow([news])


entertainmentNews = []
count = 0

paper = newspaper.build("https://indianexpress.com/section/entertainment/", memoize_articles=False)
for article_name in paper.articles:
    #article_name = Article("https://www.breitbart.com/sports/", language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    #print(article_name.title)
    entertainmentNews.append(article_name.title)
    
    if(count>10):
        break
    count = count + 1

with open('entertainmentNews.csv','w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['news'])
        for news in entertainmentNews:
            thewriter.writerow([news])
