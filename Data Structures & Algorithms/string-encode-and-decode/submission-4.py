class Solution:
    # use the format "len(s) + # + s" - m / 1 for both methods
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            enc = str(len(s)) + "#" + s
            res.append(enc)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#": j += 1
            len_st = int(s[i:j])

            i = j + 1 + len_st
            st = s[j+1:i]
            res.append(st)

        return res