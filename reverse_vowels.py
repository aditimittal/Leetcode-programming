#345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:   
        res=""
        vow=['a','e','i','o','u']
        list_vow=[]
        for i in range(0, len(s)):
            if s[i] in vow:
                list_vow.append(s[i])
        j = len(list_vow)-1
        for i in range(0, len(s)):
            if s[i] in vow:
                res +=list_vow[j]
                j-=1
            else:
                res+=s[i]
        return res