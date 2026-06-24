class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        flag = False
        for i in hash_map.values():
            if i>1:
                flag = True
                break
        return flag