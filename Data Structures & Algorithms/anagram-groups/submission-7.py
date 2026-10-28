class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            group = [0] * 26
            for c in s: group[ord(c) - ord('a')] += 1
            groups[tuple(group)].append(s)

        return list(groups.values())