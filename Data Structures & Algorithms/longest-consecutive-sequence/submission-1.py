class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        num_len = len(nums)
        longest_seq = 1

        seq = 1
        if not nums:
            return 0
            
        for i in range(num_len - 1):
            if (nums[i+1] - nums[i]) == 1:
                seq += 1
                longest_seq = max(longest_seq, seq)
 
            elif (nums[i+1] - nums[i] == 0):
                continue

            else:
                seq = 1

        return longest_seq

                