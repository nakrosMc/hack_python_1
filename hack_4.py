"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[7].upper()
    return result

hack_4 = fn_hack_4()
print(hack_4)