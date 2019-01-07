class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # if n == 0:
        #     return [0]
        # if n == 1:
        #     return [0,1]
        # part1 = self.grayCode(n-1)
        # part2 = [i + 3*pow(2,n-2) for i in part1[:len(part1)//2]]
        # part3 = [i + pow(2,n-2) for i in part1[len(part1)//2:]]
        # return part1 + part2 + part3

        res = [(i>>1)^i for i in range(pow(2,n))]
        return res
    

if __name__ == "__main__":
    solution = Solution()
    n = 2
    res = solution.grayCode(n)
    print(res)