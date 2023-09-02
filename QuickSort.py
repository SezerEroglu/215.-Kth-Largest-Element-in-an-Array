from typing import List
import random
from tests import test1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        while True:
            pivotIndex = random.randint(left, right)
            newPivotIndex = self.quickSelect(nums, left, right, pivotIndex)
            if newPivotIndex == len(nums) - k:
                return nums[newPivotIndex]
            elif newPivotIndex > len(nums) - k:
                right = newPivotIndex - 1
            else:
                left = newPivotIndex + 1

    def quickSelect(self, nums, left, right, pivotIndex):
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        storedIndex = left
        for i in range(left, right):
            if nums[i] < pivotValue:
                nums[i], nums[storedIndex], nums[storedIndex], nums[i]
                storedIndex += 1
        nums[storedIndex], nums[right] = nums[right], nums[storedIndex]
        return storedIndex


sol = Solution()

print(sol.findKthLargest(test1["test"], test1["testCount"]))
