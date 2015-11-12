#!/usr/bin/env python

# filter of cTree

import fileinput
import math
import time


errBound = 25
score = 0
candidate = set([])

def SDist(k,y):
        ans = 0
        order = 1728
        for i in xrange(4):
                t = k/order
                ans = ans + abs(t - y[-i-1])
                k = k - t*order
                order = order / 12
        return ans

def search(k, table, query, iniScore):
        filename = "treeO_"+str(k)+".txt"
        #print "searching",k
        f = open(filename,'r')

        ans = set([])

        i = f.readline()


        while (len(i)>0):
                tmpScore = iniScore

                sig = i.split()

                insID = int(sig[0])
                #print insID

                offs = 0

                for j in sig[1:]:
                        tmpScore = tmpScore + SDist(int(j),query[offs:offs+4])
                        offs = offs + 4
                        if tmpScore > errBound:
                                break

                if tmpScore<=errBound:
                        ans.add(insID)

                i = f.readline()

        f.close()

        return ans



def main():
        query = [4,6,4,5,4,4,8,6,4,4,7,5,4,6,5,5,4,3,4,8,7,7,4,2]

        qHead = query[0:4]
        start = time.time()
        
        insID = 0
        for i in fileinput.input("tree0.txt"):
                table = i.split()
                #print "------------"
                
                k = int(table[0])
                #print k
                score = SDist(int(table[0]),qHead)

                if (score<=errBound):
                        # might filter the table with hash filter
                        tmpCan = search(k, table[1:],query[4:],score)
                        if len(tmpCan) > 0:
                                #print tmpCan
                                for t in tmpCan:
                                        candidate.add(t)

                insID = insID+1

        print candidate
        print len(candidate)
        
        end = time.time()
        print end-start



if __name__ == '__main__':
        main()
