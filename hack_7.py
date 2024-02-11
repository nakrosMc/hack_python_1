"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 6
    while (i > 0):
        i -= 1
        result.append(i)
    return result

hack_7 = fn_hack_7()
print(hack_7)