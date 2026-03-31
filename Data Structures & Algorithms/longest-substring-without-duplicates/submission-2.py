class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            curr = set()
            curr.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in curr:
                    ans = max(ans, len(curr))
                    break
                curr.add(s[j])
            else:
                ans = max(ans, len(curr))
        return ans