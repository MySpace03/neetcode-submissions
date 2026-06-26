class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in ans.keys():
                return [ans[rem],i]
            ans[nums[i]] = i