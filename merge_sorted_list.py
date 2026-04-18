list1 = [1,2,4]
list2 = [1,3,4,8,9]

def mergelist(list1, list2):
    output = []
    i,j = 0,0
    if len(list1)>0 and len(list2)>0:
        while len(output)< len(list1)+len(list2):
            if i < len(list1) and j < len(list2):        
                if list1[i] != list2[j]:
                    if list1[i]<list2[j]:
                        output.append(list1[i])
                        i +=1
                    else:
                        output.append(list2[j])
                        j+=1
                else:
                    output.append(list1[i])
                    output.append(list2[j])
                    i+=1
                    j+=1
            elif i< len(list1):
                output = output+list1[i:]
            elif j < len(list2):
                output = output+list2[j:]
    else:
        output = list1+list2
    
    return output

mergelist(list1= list1, list2= list2)
