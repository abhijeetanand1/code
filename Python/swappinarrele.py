tc=int(input())
for x in range(tc):
    n=int(input("\nEnter the number of arr elements:"))
    arr=[]
    i=0
    arr=[int(s) for s in input().split()]
    while i+1<len(arr):
        arr[i],arr[i+1]=arr[i+1],arr[i]
        i=i+2
    for j in arr:
        print(j,end=' ')    