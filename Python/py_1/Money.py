Money = input()
if Money[0:3] in "RMB":
    USD = eval(Money[3:-1] + Money[-1]) / 6.78
    print("USD" + "%.2f"%USD)
else:
    RMB = eval(Money[3:-1] + Money[-1]) * 6.78
    print("RMB" + "%.2f"%RMB)
