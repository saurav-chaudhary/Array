def secondLargestElement(l):
    if len(l)==0:
        return None
    lar = l[0]
    seclar = None

    for i in l:
        if i > lar:
            seclar = lar
            lar = i
        elif i != lar:
            if seclar == None or seclar < i:
                seclar = i
    return seclar

l=[10,24,45,9,32,56,45]
print(secondLargestElement(l))
