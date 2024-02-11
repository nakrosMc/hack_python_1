"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    result = "fooziman"
    #...
    return result.upper()

hack_1 = fn_hack_1()
print(hack_1)