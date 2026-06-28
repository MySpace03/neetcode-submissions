class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] +=1
            else:
                hash_map[i] = 1
        
        ans = []
        sorted_data = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        
        for key,value in sorted_data.items():
            ans.append(key)
        return ans[:k]