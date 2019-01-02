class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # mapx = {}
        # for i in strs:
        #     tmp = ''.join(sorted(list(i)))
        #     if tmp in mapx:
        #         mapx[tmp].append(i)
        #     else:
        #         mapx[tmp] = [i]
        # return list(mapx.values())


        # import collections
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return list(ans.values()) 

        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)- ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
    

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = solution.groupAnagrams(strs)
    print(res)