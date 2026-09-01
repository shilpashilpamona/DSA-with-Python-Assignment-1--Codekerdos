class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for char in s:
            count_s = 0
            for num in s:
                if num == char:
                    count_s = count_s + 1

            count_t = 0
            for countn in t:
                if char == countn:
                    count_t = count_t + 1

            if count_s != count_t:
                return False
        return True
