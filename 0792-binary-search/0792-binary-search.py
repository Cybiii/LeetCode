class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        l = 0
        r = len(nums) - 1
        if nums[mid] == target:
            return mid
        while l <= r:
            print(l, r, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (r + l) // 2
            
        return -1 