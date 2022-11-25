# def rotateArray(arr,k,l):
#     arr2 = [0 for i in range(len(arr))]
#     for i in range(l):
#         x = (i + k) % l
#         arr2[x] = arr[i]
#     print(arr2)
# arr = [1,2,3,4,5,6,7]
# rotateArray(arr,3,len(arr))

# optimitze way
def rotateArray(arr,k,l):
    def rev(arr,l,r):
        while(l<r):
            arr[l],arr[r] = arr[r],arr[l]
            l +=1
            r -=1
    k = k % l
    rev(arr,0,l-1)
    rev(arr,0,k-1)
    rev(arr,k,l-1)
    print(arr)
arr = [1,2,3,4,5,6,7]
rotateArray(arr,3,len(arr))
