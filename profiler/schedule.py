import csv
import os
import signal
import numpy as np
import node as nd

#read mapping of APP & pid
def ReadTable():
	with open('table.csv',"r") as fp:
		reader = csv.reader(fp)
		dict={rows[0]:rows[1] for rows in reader}
	return dict 
def sendSignal(pid):
	os.kill(pid,signal.SIGUSR1)

def extractInfo():
	with open('app//app.info',"r") as fp:
		contents = fp.readlines()
		for content in contents:
			[a,b]=content.rstrip('\n').split(':')
			nd.Node()
#		print(a)
#		print(b)

dict = ReadTable()

print(dict['bfs_2'])

#ID = dict['bfs']
#sendSignal(ID);
extractInfo()

