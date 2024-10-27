class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


        # uses two pointers and a place holder.
        # assums that the first element in the array is going to be unique anyway. 
        # iterates through with two pointers and compares them to each other.
        # copies next unique num using placeholder.
