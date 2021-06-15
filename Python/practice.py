def findMaxSum(X, Y):
 
    sum = sum_x = sum_y = 0
 
    m = len(X)
    n = len(Y)
    i = j = 0

    while i < m and j < n:
        while i < m-1 and X[i] == X[i+1]:
            sum_x += X[i]
            i = i + 1
        while j < n-1 and Y[j] == Y[j+1]:
            sum_y += Y[j]
            j = j + 1
        if Y[j] < X[i]:
            sum_y += Y[j]
            j = j + 1
        elif X[i] < Y[j]:
            sum_x += X[i]
            i = i + 1
 
        else:
            sum += max(sum_x, sum_y) + X[i]
            
            i = i + 1
            j = j + 1
 
            sum_x = 0
            sum_y = 0
 
    while i < m:
        sum_x += X[i]
        i = i + 1
 
    while j < n:
        sum_y += Y[j]
        j = j + 1
 
    sum += max(sum_x, sum_y)
    return sum

a=int(input())
X=[]
for i in range(0,a):
    ele=int(input())
    X.append(ele)
b=int(input())
Y=[]
for i in range(0,b):
    ele=int(input())
    Y.append(ele)
print(findMaxSum(X,Y))    
    
    
