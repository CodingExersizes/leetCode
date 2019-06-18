'''
Given an unsorted array of integers find a pair with given sum in it.
ex:
arr =[8,7,2,5,3,1]
sum =10
'''


def findPair(arr, sum):
    hashResult ={}
    for idx, num in enumerate(arr):
        desiredInt = sum - num
        if desiredInt in hashResult:
            print ("Pair found at " ,idx," and ",  hashResult[desiredInt])
            return
        else:
            hashResult[num]=idx

    print("pair does not exist")

arr =[8,7,2,5,3,1]
sum =20
findPair(arr, sum)