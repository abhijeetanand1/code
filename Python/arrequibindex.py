tc=int(input("Enter the number of test cases :"))
for x in range(tc):
    n=int(input("\nEnter the number of arr elements :"))
    if n==0:
        print(-1)
        break
    arr=[]
    i=0
    arr=[int(s) for s in input().split()]
    lsum=0
    rsum=0
    for i in range(len(arr)):
        lsum=0
        rsum=0
        for j in range(i):
            lsum += arr[j]
        for j in range(i+1,len(arr)):
            rsum += arr[j]
        if lsum==rsum:
            print(i)
            break
    if lsum!=rsum:
        print("-1")
