def decode(instring):
    retstr = ""
    simlist = []
    simlist.extend(instring)
    for strchar in simlist:
        intchar = int(strchar)
        if (intchar - 3) < 0:
            retstr += str((intchar - 3) + 10)
        else:
            retstr += str(intchar - 3)
    return retstr