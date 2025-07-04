# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
# 2025_06_17
# Binary Search
# Template II
# Python


# Finding the lowest value of a list within a rotated list

class Solution:
    def find_min(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return left, nums[left]
    
li = [2, 3, 4, 5, 1]
sol = Solution()
print(sol.find_min(li))
    

'''
**********************************************************************************************************

2025_06_17

Finding the peak values of a list

class Solution:
    def find_peak_element(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid   
        
        return left

li = [1, 2, 3, 1, 5]
sol = Solution()
print(sol.find_peak_element(li))

**********************************************************************************************************

2025_06_15

Finding the first faulty version out of a list of versions

def is_bad_version(version: int) -> bool:
    
    if bad_version <= version:
        return True
    
    return False

class Solution:
    def first_bad_version(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2

            if is_bad_version(mid):
                right = mid
            else:
                left = mid + 1
            
        return left

bad_version = 1
versions = 1

sol = Solution()
print(sol.first_bad_version(versions))

**********************************************************************************************************
'''