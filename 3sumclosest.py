nums = [-1,2,1,-4]
target = 1

def nearest(out, target):
    I = out.values()
    I = list(I)
    if len(I)>=2:
        I.append(target)
        I.sort()
        tgt_indx = I.index(target)
        lwr = tgt_indx if tgt_indx == 0 else tgt_indx-1
        upr = tgt_indx if tgt_indx == len(I)-1 else tgt_indx+1

        diff1 = len(set(range(I[lwr],target)))
        diff2 = len(set(range(target,I[upr])))
        if diff1 != 0 and diff2 !=0:
            near = lwr if diff1 < diff2 else upr
            near = I[near]
        elif diff1 == 0 and diff2 != 0:
            near = I[upr]
        elif diff2 == 0 and diff1 !=0:
            near = I[lwr]
    else:
        near = I[0]
    return near


def Threesum(nums, vals, out, target):
    nums.sort()
    if len(nums)>3:
        for i in range(len(nums)):
            primary = nums[i]
            num = nums[i+1:]
            L = 0 
            R = len(num)-1
            
            while L < R:
                if len(num) >= 2:            
                    calc = primary+num[L]+num[R]
                    if  calc == target:
                        vals.append([primary,num[L],num[R]])
                        return calc
                    else:   
                        out[str(primary)+','+str(num[L])+','+str( num[R])] = primary+num[L]+num[R]
                        print('added')
                    if calc < target:
                        L += 1 
                    elif calc > target:
                        R -= 1
                else:
                    print('returned org list')
                    break
    else:
        return (nums[0]+nums[1]+nums[2])


def threeSumClosest(nums: list[int], target: int) -> int:
    vals = []
    out = {}
    three = Threesum(nums= nums, out= out, vals= vals, target=target)
    if three == None:
        three = nearest(out= out, target= target)
    return three

threeSumClosest(nums= nums, target= target)



def threeSumClosest(nums: list[int], target: int) -> int:
        vals = []
        out = {}
        def nearest(out, target):
            I = out.values()
            I = list(I)
            if len(I)>=2:
                I.append(target)
                I.sort()
                tgt_indx = I.index(target)
                lwr = tgt_indx-1
                upr = tgt_indx+1

                diff1 = len(set(range(I[lwr],target)))
                diff2 = len(set(range(target,I[upr])))
                near = lwr if diff1 < diff2 else upr
                near = I[near]
            else:
                near = I[0]
            return near

        def Threesum(nums, vals, out, target):
            nums.sort()
            if len(nums)>3:
                for i in range(len(nums)):
                    primary = nums[i]
                    num = nums[i+1:]
                    L = 0 
                    R = len(num)-1
                    
                    while L < R:
                        if len(num) >= 2:            
                            calc = primary+num[L]+num[R]
                            if  calc == target:
                                vals.append([primary,num[L],num[R]])
                                return calc
                            else:   
                                out[str(primary)+','+str(num[L])+','+str( num[R])] = primary+num[L]+num[R]
                                print('added')
                            if calc < target:
                                L += 1 
                            elif calc > target:
                                R -= 1
                        else:
                            print('returned org list')
                            break
            else:
                return (nums[0]+nums[1]+nums[2])
        three = Threesum(nums= nums, out= out, vals= vals, target=target)
        if three == None:
            three = nearest(out= out, target= target)
        return three

threeSumClosest(nums= nums, target= target)


