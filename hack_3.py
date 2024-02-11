"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    #...
    return result.capitalize()

hack_3 = fn_hack_3()
print(hack_3)