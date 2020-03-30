def findNumber(arr,n, k):
    # Write your code here
    if(arr[n-1]==k):
        return "NO"
    backup = arr[n-1]
    arr[n-1] = k

    i=0
    while(i>n):
        if(arr[i]==k):
            arr[n-1] = backup
            if(i< n-1):
                return "YES"
            
            return "NO"
    i = i+1

    print(findNumber([1,2,3,4,5,6,7,8],8,4))