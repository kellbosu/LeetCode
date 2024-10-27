class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        x=0
        for i in nums:
            if i==a:
                x+=1
            else:
                x-=1
            if x==0:
                a=i
                x+=1
        return a
