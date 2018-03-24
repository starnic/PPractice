TempStr = input()
if TempStr[0] in ['f', 'F']:
    C = (eval(TempStr[1:-1]+TempStr[-1])-32)/1.8
    print("C"+"%.2f"%C)
else:
    F = 1.8*eval(TempStr[1:-1]+TempStr[-1])+32
    print("F"+"%.2f"%F)
