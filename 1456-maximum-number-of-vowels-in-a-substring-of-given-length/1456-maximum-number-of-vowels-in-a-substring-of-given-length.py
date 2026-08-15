class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a','e','i','o','u']
        ans = 0
        count = 0
        i = 0

        for j in range(len(s)):
            if s[j] in v:
                count += 1

            if j-i+1 == k:
                if count > ans:
                    ans = count

                if s[i] in v:
                    count -= 1

                i = i + 1
        
        return ans