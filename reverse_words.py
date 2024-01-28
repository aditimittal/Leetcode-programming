# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        return " ".join(x[::-1])
