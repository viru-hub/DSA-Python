#https://leetcode.com/problems/3sum/submissions/1604304984/

nums = [0,0,0]

def threesum(nums):
    out = []
    if len(nums)>2:
        for i in range(len(nums)):
            primary = nums[i]
            num = nums.copy()
            num.pop(i)
            left = 0
            right = len(num)-1

            while left <= right:
                if primary+num[left]+num[right] == 0 and left != right:            
                    out.append(sorted([primary, num[left], num[right]])) if sorted([primary, num[left], num[right]]) not in out else ''
                    left +=1
                    right = len(num)-1
                else:
                    #right -=1
                    left +=1 if left >= right else 0
                    right = len(num)-1 if left >= right else right-1
    else:
        out
    
    return out

def threesum(nums):
    out = []
    nums.sort()
    if len(nums)>2:
        for i in range(len(nums)):
            primary = nums[i]
            if primary>0:break
            if i>0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = len(nums)-1

            while left < right:
                sums = primary+nums[left]+nums[right]
                if sums > 0:
                    right-=1
                elif sums <0:
                    left+=1
                else :            
                    out.append([primary, nums[left], nums[right]]) 
                    left +=1
                    right -=1
                    while left< right and nums[left-1] == nums[left]:
                        left +=1
                    while left<right and nums[right+1] == nums[right]:
                        right-=1

    else:
        out
    
    return out

threesum(nums= nums)
