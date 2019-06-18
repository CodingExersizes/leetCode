def sortBinaryArray(arr):
    zeroCounter =0

    for i in range(0, len(arr)-1):
        if arr[i]==0:
            arr[zeroCounter]=0
            zeroCounter+=1

    for k in range(zeroCounter, len(arr)-1):
        arr[k]=1

    print(arr)


sortBinaryArray([0,0,1,1,1,0,0,0,0,1])