class PrintAllSubArrays:

    def insertArr(self, hm, sum, ind):
        if sum not in hm:
            hm[sum] = [ind]
        else:
            hm[sum].append(ind)


    def printAllZeroArrays(self, arr):
        resultArrays = {}
        sum = 0
        self.insertArr(resultArrays, 0, -1 )
        for ind, num in enumerate(arr):
            sum += num
            if sum in resultArrays:
                subArr = resultArrays[sum]
                for val in subArr:
                    print("Subarray [", val+1, "...", ind, "]")
            self.insertArr(resultArrays, sum, ind)
        print(resultArrays)


pt = PrintAllSubArrays()
pt.printAllZeroArrays([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
