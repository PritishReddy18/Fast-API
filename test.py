class Solution:
    def isPalindrome(self, n):
        n = str(n)
        while len(n) > 1:
            if n[0] == n[-1]:
                n = n[1:-1]
            else:
                return False
        return True
box = Solution()
box.isPalindrome(121)