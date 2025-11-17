class Solution:
    def isThree(self, n: int) -> bool:
        k = []
        for i in range(1,n+1):
            if n%i == 0:
                k.append(i)
        
        if len(k)==3:
            return True
        else:
            return False