#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Mulitprocess version of kNN query

from multiprocessing import Pool,Manager
import os
import fileinput
import math
import time

errBound = 30
score = 0
candidate = []
candidate = Manager().list()


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
        f = open("../treeFile/"+filename,'r')

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


        if len(ans)>0:
            #print ans
            for t in ans:
                candidate.append(t)

def main(q):

        #query = [4,6,4,5,4,4,8,6,4,4,7,5,4,6,5,5,4,3,4,8,7,7,4,2]

        outf = open("queryFiles/"+q[0]+".txt",'w')
        
        query = q[1:]

        for i in xrange(24):
            query[i] = int(query[i])

        #print query




        start = time.time()

        p = Pool()

        insID = 0
        for i in fileinput.input("tree0.txt"):
                table = i.split()
                #print "------------"                
                k = int(table[0])
                score = SDist(int(table[0]),query[0:4])

                if (score<=errBound):
                        # might filter the table with hash filter
                        #print k
                        # 创建新进程
                        p.apply_async(search,args=(k, table[1:],query[4:],score))

                        # if len(threads) > 50:
                        #         for t in threads:
                        #                 t.join()
                        #         threads = []
                                
                        #tmpCan = search(k, table[1:],query[4:],score)
                        # if len(tmpCan) > 0:
                        #         #print tmpCan
                        #         for t in tmpCan:
                        #                 candidate.add(t)

                insID = insID+1
        p.close()
        p.join()

        #candidate.sort()
        for i in candidate:
            outf.write(str(i)+'\n')

        #outf.write(str(candidate)) 
        print len(candidate)
        
        end = time.time()
        print end-start



if __name__ == '__main__':

    fQuery = open('query_cSig.txt','r')
    q = fQuery.readline()
    while q:
        main(q.split())
        q = fQuery.readline()
    fQuery.close()
