def kbig (nums, k):
    k = len(nums)-k

    def quickSelect(l,r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                p += 1
        if p>k: return quickSelect(l, p-1)
        elif p<k: return quickSelect(p+1, r)
        else: return nums[p]

    return quickSelect(0, len(nums) - 1)

print (kbig ([3,2,1,5,6,4], 2))
