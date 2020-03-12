class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo=[0]
        for i in range(len(s)+1):
            for j in memo:
                if s[j:i] in wordDict:
                    memo.append(i)
                    break
        return memo[-1]==len(s)