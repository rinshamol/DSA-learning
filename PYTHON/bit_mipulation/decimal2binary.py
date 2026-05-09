a = 4294967295
def d2b(d):
    strg = ""
    while(d != 0):
        r = d%2
        strg += str(r)
        d = d//2
    print(strg[::-1])
d2b(a)
print(a.bit_length())