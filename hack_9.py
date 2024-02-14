"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    while (i < len(result)):
        result.insert(i+1,'@')
        i+=2
    return result  

hack_9 = fn_hack_9()
print(hack_9)