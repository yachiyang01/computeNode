import numpy as np
import csv

dict = {'appID':'pid'}

w = csv.writer(open('table.csv',"w"))
for key,val in dict.items():
	w.writerow([key,val])
