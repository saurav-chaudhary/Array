def largestElemet(l):
    if len(l)==0:
        return None
    lar = l[0]
    for i in range(len(l)):
        if l[i]> lar:
            lar = l[i]
    return lar
l = [2,4,1,6,7,19,32,11]
print(largestElemet(l))
