def oddNumbers(l, r):
    # Write your code here
    arr =[]
    for i in range (l,r + 1):
        if(i%2!=0):
            arr.append(i)
    return arr
           

      

print(oddNumbers(3,13))