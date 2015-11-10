#!/usr/bin/env python

# convert things into svm-light format

#<line> .=. <target> <feature>:<value> <feature>:<value> ... <feature>:<value> # <info>
#<target> .=. +1 | -1 | 0 | <float> 
#<feature> .=. <integer> | "qid"
#<value> .=. <float>
#<info> .=. <string> 

import optparse
import bz2
import sys
import os
import math

def read_label_line(flab):
	if flab:
		return flab.readline()
	else:
		return '0\n'

# binary features for dna
def convert_dna(outf, fdat, flab, num=-1):
	hashfile = file('hash.txt','wb')
	cSigfile = file('cSig.txt','wb')


	d=fdat.readline()
	l=read_label_line(flab)
	acgt=range(0,256)
	for i in xrange(256):
		acgt[i]=0
		if i==ord('C'):
			acgt[i]=1
		elif i==ord('G'):
			acgt[i]=2
		elif i==ord('T'):
			acgt[i]=3

	line=0

	q = 4 # parameter of q-gram
	n = 1
	for i in xrange(q):
		n = n*4

	while d and l and (num<0 or line<num):
		#print d
		offs=1
		s=l[:-1]
		#print line,

		qSig = []
		for i in xrange(n):
			qSig.append(0)

		for i in xrange(len(d)-q+1):
			tmp = d[i:i+q]
			#print tmp,
			r = 0
			order = 1
			for j in xrange(q):
				r = r + acgt[ord(tmp[q-j-1])]*order
				order = order * 4
			#print r
			qSig[r] = 1

			s+=" %d:1.0" % (offs+acgt[ord(d[i])])
			offs+=4
		outf.write(s + '\n')
		#print "qSig",qSig

		cSig = []

		lamda = int(round(n/22)) # lamda

		for i in range(0,n,lamda):
			tmpSum = 0
			for k in range(0,lamda):
				if (i+k == n):
					break
				tmpSum = tmpSum + qSig[i+k]
			cSig.append(tmpSum)

		#for i in cSig:
		#	cSigfile.write(str(i)+' ')
		#cSigfile.write('')

		hValue = 0
		order = 1
		for i in xrange(len(cSig)):
			if cSig[i] > 0:
				hValue = hValue + order
			order = order*2

		#hashfile.write(str(hValue)+'\n') 
		#print hValue

		d=fdat.readline()

		l=read_label_line(flab)
		line+=1;

		if not line % 1000:
			sys.stderr.write( '\r%d' % line)

def parse_options():
	parser = optparse.OptionParser(usage="%prog [options] {dna|webspam|ocr|fd|alpha|beta|gamma|delta|epsilon|zeta} {train|val|test}\n\n"
			"script convert things into svm-light format")

	parser.add_option("-o", "--outfile", type="string", default='-',
			help="""File to write the results to, default is stdout""")
	parser.add_option("-n", '--num', type="int", default=-1,
			help="extract only num many examples")
	(options, args) = parser.parse_args()

	if len(args) != 2:
		parser.error("incorrect number of arguments")

	fnames= (args[0]+'_'+args[1]+'.dat.bz2', args[0]+'_'+args[1]+'.lab.bz2')
	files=list()

	for f in fnames:
		if not os.path.isfile(f):
			if f.find('lab')>0:
				sys.stderr.write("error: no label file found, filling with zeros\n")
				files.append(None)
			else:
				parser.error("dataset %s does not exist.\n\n"
						"script must be run in the path where the data is located.\n\n" % f)
		else:
			files.append(bz2.BZ2File(f))
	if options.outfile == '-':
		outf=sys.stdout
	else:
		outf=file(options.outfile,'wb')

	return (outf, files[0], files[1], args[0], options.num)


if __name__ == '__main__':
	outf, fdat,flab,d,num=parse_options()

	if d=='dna':
		convert_dna(outf, fdat,flab, num)
