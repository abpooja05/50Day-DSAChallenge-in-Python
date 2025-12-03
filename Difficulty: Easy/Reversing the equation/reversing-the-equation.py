#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        res_str = ""
        num = ""
        
        for c in s[::-1]:
            if c == "+" or c == "-" or c == "/" or c == "*":
                num = num[::-1] # reverse digits back to normal
                res_str += num  # add the number
                num = ""        # reset
                
                #add in the result
                res_str += c    # add operator
                
            else:
                num += c
                
        num = num[::-1]
        res_str += num
        return res_str
                