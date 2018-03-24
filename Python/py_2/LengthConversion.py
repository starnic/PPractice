#长度转换，1 米 = 39.37 英寸
#m为米，in为米

l = input()
if l[-2 : ] in ["in"]:
    ml = (float(l[0 : -2])) / 39.37
    print("%.3F"%ml + "m")
if l[-1] in ["m"]:
    ml = (float(l[0 : -1])) * 39.37
    print("%.3f"%ml + "in")
