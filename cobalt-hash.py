
import os
import time
import random

def show(K, aT, bT, cT, dT, eT, fT, gT, hT):
    line = 8
    #print(a,b,c,d,e,f,g,h)
    for i in (a,b,c,d,e,f,g,h):
        line -= 1
        if(len(str(i))) < 6:
            L = len(str(i))
            while(L) < 6:
                L += 1
                print(" ", end="")
        print(i, end="")
        if(line == K):
            print(" <---", end="")

        print()

        
   
def show2():
    #print(a,b,c,d,e,f,g,h)
    for i in (A,B,C,D,E,F,G,H):

        if(len(str(i))) < 6:
            L = len(str(i))
            while(L) < 6:
                L += 1
                print(" ", end="")
        print(i, end="")
        print(" ")

def rotX(a, b, c, d, e, f, g, h):
    temp = a

    a = (b ^ c) + (d << 3)  
    b = c
    c = d
    d = (e + f + 37) % 256  
    e = f
    f = g
    g = h
    h = temp

    return a, b, c, d, e, f, g, h
#set
a = 0
b = 2
c = 0
d = 0
e = 86
f = 0
g = 0
h = 1

A,B,C,D,E,F,G,H=a,b,c,d,e,f,g,h

J = 0
K = 0

aT, bT, cT, dT, eT, fT, gT, hT = a,b,c,d,e,f,g,h
for y in range(8):
    if y != 0:
        a=a % 256  
        b=b % 256  
        c=c % 256  
        d=d % 256  
        e=e % 256  
        f=f % 256  
        g=g % 256  
        h=h % 256  

    for x in range(8):
        show(K, aT, bT, cT, dT, eT, fT, gT, hT)
        print(J)
        print(K)
        aT, bT, cT, dT, eT, fT, gT, hT = a,b,c,d,e,f,g,h

        a,b,c,d,e,f,g,h=rotX(a,b,c,d,e,f,g,h)
        
        time.sleep(0.4)
        os.system('cls')
        K += 1



    K = 0
    J += 1

    
    


print("before:")
show2()
print("now:")
show(K, aT, bT, cT, dT, eT, fT, gT, hT)