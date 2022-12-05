def feb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return feb(n-1) + feb(n-2)

n = 10
for i in range(n):
    print(feb(i))