class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for i in s:
            s_list.append(i)

        for j in t:
            t_list.append(j)

        s_list.sort()
        t_list.sort()

        if len(s_list) == len(t_list):
            if s_list == t_list:
                return True
        return False   

        