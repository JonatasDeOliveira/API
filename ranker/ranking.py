
#[(8,"cat"),(9,"sad"),(12,"cat"),(15,"bad"),(20,"cat")]


def getCovers(query, tupleList):
    ret = []
    d = {}
    lw = []
    ln = []
    n = 0
    k = 0
    for elem in query:
        d.update({elem:0})
        n += 1  
    k = n
    x = 0
    while x < len(tupleList):
        if d.has_key(tupleList[x][1]):
            if d[tupleList[x][1]] != 0:
                if lw[0] == tupleList[x][1]:
                    del lw[0]
                    del ln[0]
                    lw.append(tupleList[x][1])
                    ln.append(tupleList[x][0])
            else:
                d[tupleList[x][1]] = 1
                lw.append(tupleList[x][1])
                ln.append(tupleList[x][0])
                n -= 1
            
            if n == 0:
                n = k
                x-=k-1
                ret.append(ln)
                for elem in query:
                    d[elem] = 0
                lw = []
                ln = []
        x+=1
    return ret
    

print getCovers(["cat", "bad"],[[8,"cat"],[9,"cat"],[12,"bad"],[15,"sad"],[26,"cat"],[30,"cat"],[51,"bad"]])