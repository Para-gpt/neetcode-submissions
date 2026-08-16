class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(l, r):
            if l > r:
                return -1

            index = l + (r - l) // 2

            if nums[index] == target:
                return index

            elif nums[index] < target:
                return bin_search(index + 1, r)

            else:
                return bin_search(l, index - 1)

        return bin_search(0, len(nums) - 1)