"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    new_result = []
    for txt in result:
        if txt == 'o':
            new_result.append('0')
        elif txt == 'i':
            new_result.append('1')
        elif txt == 'a':
            new_result.append('@')
        else:
            new_result.append(txt.upper())
             
    return new_result
            
hack_10 = fn_hack_10()
print(hack_10)