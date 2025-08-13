class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1s=list(set(nums1))
        n2s=list(set(nums2))
        n3=[i for i in n1s for j in n2s if i==j]
        return n3