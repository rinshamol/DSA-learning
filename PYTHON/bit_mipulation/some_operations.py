# 1. swap 
def swap():
    a = 5 
    b = 10
    print("before: a and b:",a,b)
    a = a^b
    b = a^b
    a = a^b
    print("after: a and b:",a,b)
# 2. check ith bit is set
# right shift >>
i = 2
n = 16
def right_shift_check():
    if((n >> i) & 1):
        print("set")
    else:
        print("not set")
# left bit
def left_shift_check():
    if n & (1 << i):
        print("set")
    else:
        print("not set")
# left_shift_check()
# set ith bit
def set_bit():
    a = n |(1 << i)
    print(a)
# set_bit()
# turn off ith bit
def off_bit():
    a = n & ~(1<<i)
    print(a)
# off_bit()
# toggle ith bit
def toggle():
    a = n ^ (1<<i)
    print(a)
# toggle()
# remove the last bit
def remove_bit():
    print(n & (n-1))
# remove_bit()
# check power of 2
def pow2():
    if n & (n-1):
        print("not power")
    else:
        print("power")
# pow2()
# count the number of set bit
# method 1
def count_bit():
    count = 0
    n = 23
    while(n > 0):
        if n % 2 == 1 :
            count += 1
        n = n//2
    print(count)
# count_bit()
# method 2
def count_bit2():
    count = 0
    n = 23
    while(n > 0):
       
        count += n & 1
        n = n >> 1
    print(count)
# count_bit2()
# method 3
def count_bit2():
    count = 0
    n = 23
    while(n > 0):
        n = n & n-1
        count += 1
    print(count)
count_bit2()
