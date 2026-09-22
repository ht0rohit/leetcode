class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)

        res = 0
        m_ind = []
        currind = 0
        for i in range(n):
            
            if nums[i] == m:
                m_ind.append(i) 

            if len(m_ind) == k:
                res += m_ind[currind] + 1
            elif len(m_ind) > k:
                currind = len(m_ind) - k
                res += m_ind[currind] + 1

        return res