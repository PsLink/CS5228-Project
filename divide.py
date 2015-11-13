# divide the huge feature file into serval files

import fileinput

line = 0
filename = "DNA_feature_0.txt"
f = open(filename,'w')
for i in fileinput.input("DNA_feature"):
	line = line + 1
	f.write(i)
	if line % 5000000 == 0:
		filename = "DNA_feature_"+str(line/5000000)+".txt"
		f.close()
		f = open(filename,'w')

f.close()

