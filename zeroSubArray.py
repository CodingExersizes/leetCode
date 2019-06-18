'''
Given an array of integers, check if contains a subarray having 0 sum
'''


def zeroSubArray(arr):
    sumHash = {}
    sum = 0


    sumHash[0] = 0

    for idx, num in enumerate(arr):
        sum += num
        print(num, sum)
        if sum in sumHash.values():
            print(sumHash)
            return True
        else:
            sumHash[idx+1]= sum
    print(sumHash)
    return False



arr = [4, -2, 3, 3, -2, -1]

if zeroSubArray(arr):
    print("Yes")
else:
    print('No')


