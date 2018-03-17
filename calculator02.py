#!/usr/bin/env python3
import sys
try:
    for arg in (sys.argv[1:]):
        list=arg.split(':')
        a=int(list[0])
        b=int(list[1])
        c=b-b*0.165-3500
        if c<=1500:
            d=0
        elif c>1500 and c<=4500:
            d=c*0.1-105
        elif c>4500 and c<=9000:
            d=c*0.2-555
        elif c>9000 and c<=35000:
            d=c*0.25-1005
        elif c>35000 and c<=55000:
            d=c*0.3-2755
        elif c>55000 and c<=80000:
            d=c*0.35-5505
        else:
            d=c*0.45-13505
        s=b-d-b*0.165
        print(str(a)+':'+str(format(s,".2f")))
except ValueError:
    print("Parameter Error")

