class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = arr[0]
        for i in arr:
            if i>largest:
                largest=i
                
        secondlargest= -1
        
        for i in arr:
            if i>secondlargest and i!=largest:
                secondlargest = i
        return secondlargest
