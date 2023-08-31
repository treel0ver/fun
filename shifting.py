a=0
b=0
c=0
d=0

modi = 0

def y(x):
    return (x<<13) ^ (x<<7)

for i in range(1):
    a=2**90
    b=2**300
    c=2**202
    d=2**93

    a+= modi
    modi += 1

    for i in range(8):
        b,c,d,a=a,b,c,d

    for i in range(8):
        #print(a,b,c,d)
        b,c,d,a=y(a),y(b),y(c),(a+b+c+d) % 2**32

    #print(a,b,c,d)
    a = (95876342886945867925 + a) % 2**32
    b = (68948933427681341564 + a) % 2**32
    c = (28284852377575335433 + a) % 2**32
    d = (96749633297890450044 + a) % 2**32

    #print(a,b,c,d)
    #print(hex(a)[2:],hex(b)[2:],hex(c)[2:],hex(d)[2:])
    print((a.to_bytes(4, 'big') + b.to_bytes(4, 'big') + c.to_bytes(4, 'big') + d.to_bytes(4, 'big')).hex())
    if ((a.to_bytes(4, 'big') + b.to_bytes(4, 'big') + c.to_bytes(4, 'big') + d.to_bytes(4, 'big')).hex())[:4] == "0000":
        print(modi)
        print("__________")
        break
