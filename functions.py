def printMe(str):
    "Function to print entered line"
    print(str)
    return

printMe("Hi!")
printMe("I'm first call to user defined functions!")
printMe("I called it again!!")

def changeMe(pList):
    pList.append([1,2,3,4,5])
    print("Values inside the function: ", pList)
    return

pList = [10,20,30,40,50]    
changeMe(pList)
print("Value outside the function: ", pList)
