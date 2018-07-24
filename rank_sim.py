import requests
import json
import csv
from dandelion import DataTXT
import dandelion
import pandas as pd

#app_id = '21a98370ef2344d7aaed56d64b859342'
#app_key ='21a98370ef2344d7aaed56d64b859342'
#app_id='d99db9265bb44b898b6b18a2974029d4'
#app_key='d99db9265bb44b898b6b18a2974029d4'
#app_id = 'f915e7a160264eb7a9d0325a6e4d4456'
#app_key ='f915e7a160264eb7a9d0325a6e4d4456'
#app_id='89e955ec286c499194067f2399116beb'
#app_key='89e955ec286c499194067f2399116beb'
app_id='b653682a7ec740db87965b228972cf61'
app_key='b653682a7ec740db87965b228972cf61'
#app_id='62c1323945ce4714b1b08dd8e28dd6f3'
#app_key='62c1323945ce4714b1b08dd8e28dd6f3'
#app_id='8cd0d21d4c5d47de98fc5ac60368d17e'
#app_key='8cd0d21d4c5d47de98fc5ac60368d17e'
datatxt = DataTXT(app_id='b653682a7ec740db87965b228972cf61',app_key='b653682a7ec740db87965b228972cf61')
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
