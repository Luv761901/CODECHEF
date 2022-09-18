try:
    x, y = map(float, input().split())
    if x <= y-0.5 and x % 5 == 0:
        print("%.2f" % (y-x-0.50))
    else:
        print("%.2f" % y)

except:
    pass
