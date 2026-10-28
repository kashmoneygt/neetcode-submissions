class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#": j += 1

            size = int(s[i : j])

            i = j + size + 1
            item = s[j + 1 : i]
            res.append(item)

        return res

