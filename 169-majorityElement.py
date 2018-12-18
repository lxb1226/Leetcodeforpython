class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # import operator
        # counts = {}
        # for num in nums:
        #     count = 1
        #     if num in counts.keys():
        #         counts[num] += count
        #     else:
        #         counts[num] = count
        
        # return sorted(zip(counts.values(),counts.keys()),reverse=True)
        # # return sorted(counts.items(),key=lambda x:x[1],reverse=True)[0][0]
        # # return sorted(counts.items(),key=operator.itemgetter(1),reverse=True)[0][0]


        # ## 以上代码的变形
        # lookup = {}
        # for num in nums:
        #     lookup[num] = lookup.get(num,0) + 1
        # max_occur = max(lookup.values())
        # for key in lookup:
        #     if lookup[key] == max_occur:
        #         return key

        # ## 整合后的代码
        # import operator
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num,0) + 1
        # return sorted(counts.items(),key=operator.itemgetter(1),reverse=True)[0][0]


        ## boyer-Moore众数问题(majority number)
        ## 在数组中找到两个不相同的元素并删除它们，不断重复此过程，知道数组中元素都相同，那么剩下的就是主要元素
        count,candidate = 0,None
        for num in nums:
            if count == 0:
                candidate = num
            count = count + 1 if num == candidate else count -1
        return candidate
    

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,3]
    result = solution.majorityElement(nums)
    print(result)
