import operator
import csv
inputFile=raw_input("Enter the csv file to be ranked:")
inp=inputFile+"_results.csv"
reader=csv.reader(open(inp),delimiter="|")
sortedList=sorted(reader,key=lambda row:row[3],reverse=True)
outputFile=inputFile+"_sorted.csv"
with open(outputFile,"w") as f:
	f.write("Similarity|Number|Text|Id")
	f.write('\n')
	for row in sortedList:
		f.write(str(row[3]))
		f.write("|")
		f.write(row[0])
		f.write("|")
		f.write(row[1])
		f.write("|")
		f.write(row[2])
		f.write('\n')
	#print('\n')
