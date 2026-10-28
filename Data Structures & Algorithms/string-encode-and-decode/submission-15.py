class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#": j += 1
            cnt = int(s[i : j])
            
            item = s[j + 1 : j + 1 + cnt]
            res.append(item)

            i = j + 1 + cnt

        return res
