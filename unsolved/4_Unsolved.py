class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merge = []
        lena = len(nums1)
        lenb = len(nums2)
        lentotal = lena + lenb
        i = j = 0
        for k in range(0, lentotal):
            if i == lena:
                merge.extend(num2[j:])
                break
            elif j == lenb:
                merge.extend
