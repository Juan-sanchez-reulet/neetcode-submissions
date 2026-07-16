class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0,len(nums)-1
        while L<=R:
            middle = (L+R)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                L=middle+1
            else:
                R=middle-1
        return -1

