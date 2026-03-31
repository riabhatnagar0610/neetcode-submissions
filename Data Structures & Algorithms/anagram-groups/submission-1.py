class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            sub = "".join(sorted(word))
            ans[sub].append(word)
        return list(ans.values())
        