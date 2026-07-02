class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        arr = list(set(nums))
        arr.sort()

        counter = 1
        ans = 1

        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i] + 1:
                counter += 1
            else:
                ans = max(ans, counter)
                counter = 1

        ans = max(ans, counter)
        return ans
