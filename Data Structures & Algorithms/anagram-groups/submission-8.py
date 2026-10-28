class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key not in groups:
                groups[key] = []

            groups[key].append(str)
        
        return list(groups.values())