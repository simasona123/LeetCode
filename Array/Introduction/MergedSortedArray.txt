class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        for i in range (m+n+1, -1, -1):
            if m == -1:
                nums1[:i+1] = nums2[:n+1]
                break
            elif n == -1 :
                pass
            elif nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            elif nums2[n] >= nums1[m]:
                nums1[i] = nums2[n]
                n -= 1
            # print(nums1)