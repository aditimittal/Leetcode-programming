#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1: int = len(word1)
        len_word2: int = len(word2)
        min_len=min(len_word1, len_word2)
        result=""
        for i in range(0,min_len):
            result+=word1[i]
            result+=word2[i]
        if min_len<len_word1:
            result += word1[min_len:]
        elif min_len<len_word2:
            result += word2[min_len:]
        print(result)
        return result
    
