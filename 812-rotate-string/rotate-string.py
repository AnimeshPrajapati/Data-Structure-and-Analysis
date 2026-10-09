class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss=s+s
        if len(s)!= len(goal):
            return False
        else:
            if goal in ss:
                return True
            else:
                return False
        