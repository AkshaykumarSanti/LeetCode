class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        
        ans = 0
        push = 1

        while n > 8:
            ans += 8 * push
            n = n - 8
            push = push + 1

        ans += n * push

        return ans  
        


        
        