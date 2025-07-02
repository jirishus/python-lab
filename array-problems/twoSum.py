from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    # If no valid pair is found, return an empty list
    return []


# Test cases
s = Solution()
assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
assert sorted(s.twoSum([3, 2, 4], 6)) == [1, 2]
assert sorted(s.twoSum([3, 3], 6)) == [0, 1]

print("All tests passed.")