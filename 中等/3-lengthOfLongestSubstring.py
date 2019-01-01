class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # l,start,n = 0,0,len(s)
        # maps = {}
        # for i in range(n):
        #     start = max(start,maps.get(s[i],-1) + 1)
        #     l = max(l,i-start+1)
        #     maps[s[i]] = i
        # return l

        lookup = {}
        start, end, counter, length = 0, 0, 0, 0
        while end < len(s):
            lookup[s[end]] = lookup.get(s[end], 0) + 1
            if lookup[s[end]] == 1:
                counter += 1
            end += 1
            while start < end and counter < end - start:
                
                lookup[s[start]] -= 1
                if lookup[s[start]] == 0:
                    counter -= 1
                start += 1
            length = max(length, end - start)
        return length


if __name__ == "__main__":
    solution = Solution()
    s = 'xyzxlkjh'
    result = solution.lengthOfLongestSubstring(s)
    print(result)
   
