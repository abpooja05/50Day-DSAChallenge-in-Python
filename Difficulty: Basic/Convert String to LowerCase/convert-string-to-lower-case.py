class Solution:
    def toLower (self , s : str)-> str :
        #code here 
        res = []
        for i in s:
            lower = i.lower()
            res.append(lower)
        return "".join(res)