
file = open('floridamantweets.txt', 'r')

tweets = file.read().splitlines()
print len(tweets)
tweets_without_links=[]

for tweet in tweets:
    if tweet.find('|') > 0:
        b=tweet.find('|')
        a = tweet[:b]
        tweets_without_links.append(a)
    elif tweet.find('http') > 0:
        b=tweet.find('http')
        a = tweet[:b]
        tweets_without_links.append(a)
    else:
        tweets_without_links.append(tweet)

f=open('cleantweets.txt','w')
for tweet in tweets_without_links:
    f.write(tweet + '\n')
