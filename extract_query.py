# extract cSig&Hash value of +1 instance as query point

import fileinput

# extract +1 instance
# line = 0
# f = open("tmp.txt",'w')
# for i in fileinput.input("feature_10w"):
# 	line = line + 1
# 	tmp = i.split()
# 	if tmp[0] == "+1":
# 		f.write(i)
# f.close()

name = "cSig" #input("Input the filename: hash/cSig")
line = 0

q = open("query_id.txt",'r')
query = int(q.readline())
out = open("query_"+name+".txt",'w')
for i in fileinput.input(name+".txt"):
	if query == line :
		out.write(str(query)+' '+i)
		if query == 49999815:
			break
		query = int(q.readline())
	line = line + 1
out.close()