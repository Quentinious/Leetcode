"""
  Do not return anything, modify nums1 in-place instead.
  """

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m-1
    j = n-1
    k = m+n-1

    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums2[j]
            j-=1
        elif nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        k-=1
    print(nums1)
    print(nums2)
    # nums1 = [2,5,6,0,0,0]
    # nums2 = [1,2,3]
    # j=i
    # while j >= 0:
    #     nums1[k] = nums2[j]
    #     k-=1
    #     j-=1
    while j >= 0:
        nums1[k] = nums2[j]
        k-=1
        j-=1

    print(nums1)
    print(nums2)


# merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([2,5,6,0,0,0], 3, [1,2,3],3)
# nums1 = [1, 2, 3, 0, 0, 0], # m = 3,
# nums2 = [2, 5, 6], n = 3