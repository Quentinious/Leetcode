def runningSum(nums: list[int]) -> list[int]:
    for x in range(1,len(nums)):
        nums[x]+=nums[x-1]

    return nums



print(runningSum([1,2,3,4]))
