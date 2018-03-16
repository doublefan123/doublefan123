#!/usr/bin/env python3
import sys
try:
    a=int(sys.argv[1])
    b=3500
    c=a-b
    if c<=1500:
        print(format(0,".2f"))
    elif c>1500 and c<=4500:
        d=c*0.1-105
        print(format(d,".2f"))
    elif c>4500 and c<=9000:
        d=c*0.2-555
        print(format(d,".2f"))
    elif c>9000 and c<=35000:
        d=c*0.25-1005
        print(format(d,".2f"))
    elif c>35000 and c<=55000:
        d=c*0.3-2755
        print(format(d,".2f"))
    elif c>55000 and c<=80000:
        d=c*0.35-5505
        print(format(d,".2f"))
    else:
        d=c*0.45-13505
        print(format(d,".2f"))
except ValueError:
    print("Parameter Error")

