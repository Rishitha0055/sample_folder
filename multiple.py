 
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Driver code
list1 = [4, 5, 7]
list2 = [3, 4, 5]
print(multiplyList(list1))
print(multiplyList(list2))