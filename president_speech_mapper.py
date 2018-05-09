import tweepy
import csv

consumer_key = 'tDnNcHt4xSPI6oEkCyLe2AMgF'
consumer_secret = 'A3tDeC80iIlZVewNWvY2d0rNxdSMpGvqDI1fiHZixGzHcSiHdq'

access_token = '346254841-yeTkUEVy84okfDL9v0pVrQjlDyckaYOgvz6JN11G'
access_token_secret = 'ObqW5Ra77HA3x2npYC4Kxlgjv5jnbdTIClLhWrtBOIfMP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#profiles of iterest
candidates = {'Jair Bolsonaro':['jairbolsonaro'], 'Joao Amoedo': ['joaoamoedonovo'], 
					#'Geraldo Alckmin': ['geraldoalckmin'], 'Henrique Meirelles':['meirelles'], 
					#'Flavio Rocha': ['flaviogr'], 'Alvaro Dias': ['alvarodias_'],'Lula': ['LulapeloBrasil'],
					'Guilherme Boulos': ['GuilhermeBoulos'], 'Marina Silva': ['silva_marina'], 'Joaquim Barbosa': ['joaquimboficial'],
					'Rodrigo Maia': ['RodrigoMaia'], }

#words to be searched
subjects = {'Deus': ['deus'], 
			'riqueza': ['riqueza'],
			'Liberdade': ['liberdade'],
			'Pobreza': ['pobreza'],
			'Sexo': ['sexo',]}


#get user's tweets
for value in candidates.keys():
	print(value)
	tweets_list = []

	candidate_tweets = api.user_timeline(id = candidates[value][0], count = 200, include_rts = True)
	#for status in candidate_tweets:
	#	tweets_list.append(status.text.lower())
	for status in tweepy.Cursor(api.user_timeline, id = candidates[value][0], count = 200, include_rts = True, ).items():
		tweets_list.append(status._json['text'].lower())
	ind_ex = 0

	print(len(tweets_list))
	candidates[value].append(len(tweets_list))

	#search for the words that are in the dictionary in the candidade's tweet's
	for key in subjects.keys():
		for subject in subjects[key]:
			for i in range(0, len(tweets_list)):
				ret = tweets_list[i].find(subject)
				if ret > 0:
					ind_ex += 1
		candidates[value].append(ind_ex)
		ind_ex = 0

#create the header of the spreadsheet
header = ['', 'Quantidade de tweets lidos']
for value in subjects.keys():
    header.append(value)

#put the results in a .csv file
with open('results.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(header)
    for key, value in candidates.items():
    	spamwriter.writerow(value)
