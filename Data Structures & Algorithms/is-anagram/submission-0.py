class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}                         #created to count chars how many times s,t appears... 

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i] , 0)         #if count is 0 then its true 
            countT[t[i]] = 1 + countT.get(t[i] , 0)

        return countS == countT