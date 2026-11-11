def twoSum(numbers: list[int], target: int) -> list[int] | None:
    i = 0
    j = len(numbers) - 1
    while i < j:
        temp = numbers[i] + numbers[j]
        if temp == target:
            return [i+1,j+1]
        if temp < target:
            i += 1
        else:
            j -= 1

    return None



print(twoSum(numbers = [2, 7, 11, 15], target = 9))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [-1,0], target = -1))



# Input: numbers = [2, 7, 11, 15], target = 9
#     Output: [1, 2]
#     Explanation: The
#     sum
#     of
#     2 and 7 is 9.
#     Therefore, index1 = 1, index2 = 2.
#     We
#     return [1, 2].
# numbers = [2,3,4], target = 6