nums1 = [4,0,0]
m = 1
nums2 = [2,5]
n = 2
k=0
for i in range(m, len(nums1)):
    nums1[i] = nums2[k]
    k += 1
nums1 = sorted(nums1)
nums1.sort()