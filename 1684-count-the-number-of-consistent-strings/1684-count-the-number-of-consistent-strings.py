class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            mark = 0
            for i in word:
                if i not in allowed:
                    mark = 1
            
            if mark == 0:
                count += 1
        
        return count