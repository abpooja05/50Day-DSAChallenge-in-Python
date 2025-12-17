class Solution:
 
    def mergeSort(self,arr, l, r):
         #code here
        def merge(arr,l,m,r):
            temp=[]
            start=l
            end=m+1
            while start<=m and end<=r:
                if arr[start]<=arr[end]:
                    temp.append(arr[start])
                    start+=1
                else:
                    temp.append(arr[end])
                    end+=1
            while start<=m:
                temp.append(arr[start])
                start+=1
            while end<=r:
                temp.append(arr[end])
                end+=1
            for i in range(l,r+1):
                arr[i]=temp[i-l]
            return arr
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
                
                
        
