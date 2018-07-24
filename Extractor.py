import sys,getopt,datetime,codecs
from datetime import datetime,timedelta
import tweet

def main(argv):

	if len(argv) == 0:
		print('Please pass some parameters!.')
		return
	try:
		opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output="))

		tweetCriteria = tweet.manager.TweetCriteria()
		outputFileName = "test.csv"
		flag=0

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg

			elif opt == '--since':
				tweetCriteria.since = arg
				sinceTime=tweetCriteria.since
				#untilTime=datetime.strptime(str(sinceTime),'%Y-%m-%d')+timedelta(days=50)
				#finalTime=untilTime.strftime('%Y-%m-%d')
				#tweetCriteria.until=finalTime

			elif opt == '--until':
				tweetCriteria.until = arg

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
			
			elif opt == '--near':
				tweetCriteria.near = '"' + arg + '"'
			
			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--output':
				outputFileName = arg
	
		outputFile = codecs.open(outputFileName, "w+", "utf-8")

		outputFile.write('username|date|retweets|favorites|text|geo|mentions|hashtags|id|permalink')

		print('Extracting the tweets from twitter! Please wait...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('\n%s|%s|%d|%d|"%s"|%s|%s|%s|"%s"|%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
			outputFile.flush()
			print('More %d tweets saved on file...\n' % len(tweets))

		tweet.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except arg:
		print('Arguments parser error.Please try again!' + arg)
	finally:
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
	main(sys.argv[1:])
