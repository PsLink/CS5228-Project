#!/usr/bin/env python
# coding=utf-8

# Retrive same amout +1/-1 label from the kNN result

import fileinput

name = "26073"

candidate = set([])

for i in fileinput.input("query_id.txt"):
	candidate.add(i)

outf = open(name,"w")
cP = 0
cM = 0

for i in fileinput.input(name+".txt"):
	if i in candidate:
		outf.write(i)
		cP = cP+1
	elif cM < cP:
		outf.write(i)
		cM = cM + 1

outf.close()




    

