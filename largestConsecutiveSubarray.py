def largestSubarray(arr):
    '''
    Given an  array of integers, fine largest subarrat formed by consecuitive numbers.
    Sub-array should contain all distinct values
    :param arr:
    :return:

    edge cases to consider - negarive numbers
    '''

    firstind =0
    lastind =len(arr)-1
    result =[]

    while firstind !=lastind:
        print("ind", firstind, lastind)
        dist = abs(arr[lastind] -arr[firstind])

        if dist > lastind-firstind:
            lastind -=1
            continue
        else:
            '''check if consecutive'''
            sortedArr = sorted(arr[firstind:lastind])
            ll =len(sortedArr)
            isConseq=True
            for i in range(0, ll):
                if sortedArr[i+1] - sortedArr[i]!=1:
                    firstind +=1
                    isConseq = False
                    break
            if(isConseq):
                print("Found")
                result = arr[firstind:lastind]
                lastind =firstind



    return result


largestSubarray([2,0,2,1,4,3,1,0])







