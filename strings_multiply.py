num1 = "0"
num2 = "0"

num1 = "0"
num2 = "345"
def string_multiply(num1, num2):
    todo = [num1, num2]
    values = []
    for K in todo:
        Actual = 0
        length = len(K)
        supportive = 1
        #6*(10**(len(k)-2))
        for j in K:
            for i in range(0,10):
                if str(i) == j:
                    #print(i)
                    Actual += i*(10**(length-supportive))
                    supportive += 1
                    break
                else:
                    pass
        values.append(Actual)

    output = values[0]*values[1]
    return str(output)

string_multiply(num1, num2)

