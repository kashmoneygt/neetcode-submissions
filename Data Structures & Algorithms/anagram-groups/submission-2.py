class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap - n / n
        groups = {}
        for s in strs:
            group = [0] * 26
            for c in s: group[ord(c) - ord('a')] += 1
            group = tuple(group)

            if group not in groups: groups[group] = []
            groups[group].append(s)

        return list(groups.values())