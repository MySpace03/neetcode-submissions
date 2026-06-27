class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        for i in range(len(strs)):
            temp_for_ans = []
            if any(strs[i] in row for row in ans):
                continue
            else:
                temp_for_ans.append(strs[i])
                temp = sorted(strs[i])
            for j in range(i+1,len(strs)):
                if temp == sorted(strs[j]):
                    temp_for_ans.append(strs[j])
            ans.append(temp_for_ans)
        return ans
