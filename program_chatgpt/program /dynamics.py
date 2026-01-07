def logistic(x,r=4.0): return r*x*(1-x)
x=0.123456
print([int((x:=logistic(x))*10) for _ in range(50)])
