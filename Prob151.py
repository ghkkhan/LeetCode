class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        s = ""
        for i in range(len(lst)):
            s += lst[len(lst) - 1 - i] + " "
        return(s.strip())