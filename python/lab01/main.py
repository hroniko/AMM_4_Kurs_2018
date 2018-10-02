
def funcX(x):
    return 5*x-10

def findPoint(a, b, delta):
    AA = funcX(a)
    BB = funcX(b)
    c = (a+b) / 2
    CC = funcX(c)
    if (abs(b-a) <= delta):
        return (c, CC)
    if (AA*BB)>0:
        return (None, None)
    if (AA*CC) < 0:
        return findPoint(a, c, delta)
    if (CC*BB) < 0:
        return findPoint(c, b, delta)

def cellPoint(a, b, h, delta):
    resultList = []
    ai = a - h
    bi = a
    while bi <= b:
        ai = ai + h
        bi = ai + h
        AA = funcX(ai)
        BB = funcX(bi)
        if (AA*BB) < 0:
            resultList.append(findPoint(ai, bi, delta))
    return resultList



if __name__ == '__main__':
    print(cellPoint(0.0, 50.0, 5, 0.0001))