#!/usr/bin/env python

# pickup the +1 examples in the original data

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
	queryfile = file('query.txt','wb')


	#d=fdat.readline()
	l=read_label_line(flab)

	line=0

	while d and l and (num<0 or line<num):
		#print d
		offs=1
		s=l[:-1]

		if s=="+1":
			print line

		#d=fdat.readline()

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
