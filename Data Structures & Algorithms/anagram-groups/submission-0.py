from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resHash = defaultdict(list)
        res = []

        for s in strs:
            sortedS = "".join(sorted(s))
            resHash[sortedS].append(s)
        for key in resHash:
            res.append(resHash[key])
        return res