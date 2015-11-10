#!/usr/bin/env python

# convert cSig to "cTree"
import fileinput

treeSize = 20737
BASE = 12

height = 4
tree0 = []
treeOther = []

for i in xrange(treeSize):
	tree0.append(set([]))

# def transback(k): #need to reverse back
# 	ans = []
# 	order = 1728
# 	while order >= 1:
# 		ans.append(k/order)
# 		k = k % order
# 		order = order / 12
# 	print ans

def treeHead(sig,idNum):
	k = 0
	order = 1
	for i in sig:
		k = k + int(i)*order
		order = order * BASE
	tree0[k].add(idNum)


def treeInsert(sig,idNum):
	k = 0
	order = 1
	for i in sig:
		k = k + int(i)*order
		order = order * BASE
	treeOther[idNum].append(k)


def main():
	tree0file = file('tree0.txt','wb')
	#treeOtherfile = file('treeOther.txt','wb')
	insID = 0

	for i in fileinput.input("cSig.txt"):
		i = i.split()
		treeHead(i[0:height],insID)
		
		treeOther.append([])
		for j in range(height,24,height):
			treeInsert(i[j:j+height],insID)

		#print insID,treeOther[insID]
		#print "----"

		insID = insID + 1

	for i in xrange(treeSize):
		if (len(tree0[i]) > 0):
			tree0file.write(str(i)+' ')

			filename = 'treeO_' + str(i) + '.txt'

			outf = open(filename,'w')
			for  j  in tree0[i]:
				tree0file.write(str(j)+' ')
				outf.write(str(j)+' ')
				for k in treeOther[j]:
					outf.write(str(k)+' ')
				outf.write('\n')
				#print j,treeOther[j]
			#print 
			outf.close()
			tree0file.write('\n')




		

if __name__ == '__main__':
	main()