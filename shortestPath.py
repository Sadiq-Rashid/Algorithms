coins = "dabbcabcd"
newString = str()
letterSet = set()
for letter in coins:
    letterSet.add(letter)
windowSize = len(letterSet)
foundInWindow = False
while(True):    
    for i in range(len(coins)-windowSize+1):
        allLetters = True
        newSubString = coins[i:i+windowSize]
        for letter in letterSet:
            if(letter not in newSubString):
                allLetters = False
        if(allLetters == True):
            newString = newSubString
            foundInWindow = True
            break
    if(foundInWindow == True):
        break
    else:
        windowSize+=1
print(newString)

        



print(newString)