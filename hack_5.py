"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    new_result = ""
    for txt in result:
        if (txt == 'o'):
            new_result += '0'
        elif (txt == 'i'):
            new_result += '1'
        elif (txt == 'a'):
            new_result+= '@'
        else:
            new_result += txt
    return new_result

hack_5 = fn_hack_5()
print(hack_5)