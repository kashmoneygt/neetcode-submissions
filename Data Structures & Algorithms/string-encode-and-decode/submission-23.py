class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            
            len_sub = int(s[i:j])
            sub = s[j + 1 : j + 1 + len_sub]
            res.append(sub)
            i = j + 1 + len_sub
        
        return res
