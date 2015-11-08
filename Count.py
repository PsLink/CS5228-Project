import fileinput

count = set([])
for line in fileinput.input("inter"):
	count.add(line)

print len(count)