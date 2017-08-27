
def answer(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    newstr = ''
    for lt in s:
        if lt not in abc:
            newstr = newstr + lt
        else:
            newstr = newstr + abc[len(abc) - abc.index(lt) - 1]
    return newstr