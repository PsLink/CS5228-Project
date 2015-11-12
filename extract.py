# extract +1 instance

import fileinput

line = 0
f = open("tmp.txt",'w')
for i in fileinput.input("feature_10w"):
	line = line + 1
	tmp = i.split()
	if tmp[0] == "+1":
		f.write(i)
f.close()

