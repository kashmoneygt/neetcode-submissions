class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1 # increment left open (both min and max)
                leftMax += 1
            elif c == ")":
                leftMin -= 1 # decrement left open (both min and max)
                leftMax -= 1
            else:
                leftMin -= 1 # decrement min to treat * as )
                leftMax += 1 # increment max to treat * as (
            
            if leftMax < 0: # too many ), not enough (
                return False
            if leftMin < 0: # for the case like s = ( * ) (
                leftMin = 0
        
        return leftMin == 0
