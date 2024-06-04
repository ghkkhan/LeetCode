class Solution:
    def reverseVowels(self, s: str) -> str:
        svi = 0
        lvi = len(s) - 1
        s = list(s)
        vovels = {'a', 'e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(len(s)):
            if s[svi] in vovels:
                for j in range(len(s)):
                    if s[lvi] in vovels:
                        temp = s[svi]
                        s[svi] = s[lvi]
                        s[lvi] = temp
                        print(svi, lvi)
                        lvi -= 1
                        break
                    else:
                        lvi -= 1
                    if lvi <= svi:
                        break
                if lvi <= svi:
                        break
                svi += 1
            else:
                svi += 1
        return (''.join(s))