from sys import stdin
def maxDistance(arr, n):
    mp = {}
    maxDict = 0
    for i in range(n):
        if arr[i] not in mp.keys():
            mp[arr[i]] = i
        else:
            maxDict = max(maxDict, i-mp[arr[i]])
 
    return maxDict
def takeInput():
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n    

arr,n=takeInput() 
n = len(arr)
print (maxDistance(arr, n))