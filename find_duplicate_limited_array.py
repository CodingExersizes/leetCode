"""
Given a limited range array of size n where array contains elements between 1 to n-1
with one elelment repeating, find the duplicate element in it.
"""


def findDuplicate(arr):
    expectedSum = len(arr)/2 * (len(arr) -1)
    actualSum = sum(arr)

    print(actualSum, expectedSum, len(arr))

    return actualSum-expectedSum

def findDuplicate_xor(arr):


    for i  in range(0, len(arr)):
        xor = 0
        print(xor, arr[i])
        xor ^=arr[i]
        print(xor)

    for i in range(1, len(arr)-1):

        print(xor, i)
        xor ^=i
        print(xor)

    return xor
print("the dup is:", findDuplicate([1,2,2,3,4,]))
# print("the dup is:", findDuplicate_xor([1,2,3,4,5]))


