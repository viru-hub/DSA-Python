from typing import List
nums = [0,0,1,1,1,2,2,3,3,4]
nums

def removeDuplicates(nums: List[int]) -> int:
    output = []
    for i in range(1,len(nums)):
        if nums[i] not in output:
            output.append(i)
        if nums[i-1] == nums[i]:
            nums.append(nums[i])
            nums.pop(i)           
        elif i >= 2 and nums[i-2] == nums[i-1]:
            nums.append(nums[i-2])
            nums.pop(i-2)
            pass
    return len(output)


def removeDuplicates(nums):
    Duplicates = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] or nums[i] in Duplicates:
            Duplicates.append(nums[i])
            nums[i] = "Duplicate"

    nums = [item for item in nums if item != "Duplicate"]
    k = len(nums)
    nums = nums+Duplicates
    return k

removeDuplicates(nums= nums)