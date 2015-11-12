#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import fileinput
import math
import time

errBound = 25
score = 0
candidate = set([])
threadLock = threading.Lock()

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, k, table, query, s):
        threading.Thread.__init__(self)
        self.threadID = k
        self.table = table
        self.query = query
        self.socre = s
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        #print "Starting " + str(self.threadID)
        # 获得锁，成功获得锁定后返回True
        threadLock.acquire()
        search(self.threadID, self.table, self.query, self.socre)
        # 释放锁
        threadLock.release()
        #print "Exiting " + str(self.threadID)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


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

        if len(ans)>0:
                for t in ans:
                        candidate.add(t)

def main():
        query = [4,6,4,5,4,4,8,6,4,4,7,5,4,6,5,5,4,3,4,8,7,7,4,2]

        start = time.time()

        threads = []

        insID = 0
        for i in fileinput.input("tree0.txt"):
                table = i.split()
                #print "------------"                
                k = int(table[0])
                score = SDist(int(table[0]),query[0:4])

                if (score<=errBound):
                        # might filter the table with hash filter
                        #print k
                        # 创建新线程
                        threads.append(myThread(k, table[1:],query[4:],score))
                        # 开启线程
                        threads[-1].start()

                        if len(threads) > 50:
                                for t in threads:
                                        t.join()
                                threads = []
                                
                        #tmpCan = search(k, table[1:],query[4:],score)
                        # if len(tmpCan) > 0:
                        #         #print tmpCan
                        #         for t in tmpCan:
                        #                 candidate.add(t)

                insID = insID+1


        # 等待所有线程完成
        for t in threads:
            t.join()

        print candidate
        print len(candidate)
        
        end = time.time()
        print end-start



if __name__ == '__main__':
        main()
