def pivotIndex(nums: list[int]) -> int:
    leftSum = [0] * len(nums)
    rightSum = [0] * len(nums)

    leftSum[0] = nums[0]
    for x in range(1, len(nums)):
        leftSum[x] = nums[x] + leftSum[x - 1]

    rightSum[-1] = nums[-1]
    for x in range(len(nums) - 2, -1, -1):
        rightSum[x] = rightSum[x + 1] + nums[x]

    for x in range(len(nums)):
        if leftSum[x] == rightSum[x]:
            return x

    return -1