 
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
     
# Driver code
list1 = [10, 5, 7]
list2 = [3, 4, 8]
print(multiplyList(list1))
print(multiplyList(list2))