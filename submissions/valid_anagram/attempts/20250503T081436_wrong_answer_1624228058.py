class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = list(s), list(t)
        for elem in t_list:
            if elem in s_list:
                del s_list[s_list.index(elem)]

        if s_list:
            return False
        else:
            return True