class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))

        # reverse num1 and num2
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                # i1+i2 = the place to put digit (could be 1 or 2 digit value)
                # there may already be a carry there so use +=
                res[i1 + i2] += digit

                # from ones place, calculate carry and put in tens place
                res[i1 + i2 + 1] += res[i1 + i2] // 10

                # in ones place, keep the ones place of digit only
                res[i1 + i2] %= 10

        # reverse our res and get rid of leading 0s
        res, begin = res[::-1], 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        
        # convert each int to string for the non-0 part of res
        res = map(str, res[begin:])
        return "".join(res)

