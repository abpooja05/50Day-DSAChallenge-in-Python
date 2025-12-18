
class Solution:
    #code here
    def quickSort(self,arr,low,high):
        if low>=high:
            return
        pivotI=self.partition(arr,low,high)
        self.quickSort(arr,low,pivotI-1)
        self.quickSort(arr,pivotI+1,high)
    
    def partition(self,arr,low,high):
        #code here
        pivot=arr[low]
        i=low
        j=high
        while i<j:
            while i<high and arr[i]<=pivot:
                i+=1
            while j>low and arr[j]>pivot:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
    

    
