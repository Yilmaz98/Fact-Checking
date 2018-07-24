import requests
import json
import csv
from dandelion import DataTXT
import dandelion
import pandas as pd

datatxt = DataTXT(app_id='',app_key='ENTER YOUR TWITTER API KEY')
if __name__=='__main__':
	query1=raw_input("Enter the input claim:")
	inputFile=raw_input("Enter the file name to be checked for:")
	inputFile=inputFile+".csv"
	colnames=["username","date","retweets","favorites","text","geo","mentions","hashtags","id","permalink"]
	with open(inputFile) as csvfile:
		inputReader=pd.read_csv(csvfile,sep="|",error_bad_lines=False)
		textReader=inputReader['text']
		outputFile=inputFile.split('.')[0]+"_results.csv"
		with open(outputFile,"w") as f:
			try:
				for i in range(0,inputReader.shape[0]):
					query2=textReader[i]
					print(query2)
					try:
						response=datatxt.sim(query1,query2)
						if response.similarity>0.4:
                                                	f.write(str(i))
                                                	f.write('|')
                                                	f.write(query2)
                                                	f.write('|')
                                                	f.write(str(inputReader['id'][i]))
                                                	f.write('|')
                                                	f.write(str(response.similarity))
                                                	f.write('\n')
					except Exception as e:
						print str(e)
			except dandelion.base.DandelionException as e:
					print "No Units Left"
		f.close()
