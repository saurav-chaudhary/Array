def nextSmallestElement(A,k):
    A.sort()
    if k > max(A):
       return (max(A))
    for i in range(len(A)):
        if i == 0 and A[i] == k:
            return -1

        if A[i]< k and k < A[i+1]:
            return A[i]

a= [13,21,45,32,78,2]
k =79
print(nextSmallestElement(a,k))
