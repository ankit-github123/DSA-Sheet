class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] < min:
                min = nums[mid]
            if nums[high]>= nums[mid]:
                high = mid-1
            else:
                low = mid +1
        return min
                
        