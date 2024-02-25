"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    new_result = result.replace("fooziman","F00Z1M@N")
    ls = list(new_result)
    return ls

hack_10 = fn_hack_10()
print(hack_10)