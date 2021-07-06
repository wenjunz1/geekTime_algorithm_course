class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        table = dict()
        table[0] = 1
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(sums)):
            sums[i] = sums[i - 1] + nums[i - 1]
            if (sums[i] - k) in table:
                ans += table[sums[i] - k]
            if sums[i] in table:
                table[sums[i]] = table[sums[i]] + 1
            else:
                table[sums[i]] = 1
        return ans
