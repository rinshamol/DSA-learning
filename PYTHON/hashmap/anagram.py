s1 = "listen"
s2 = "silent"
# Should return True

# s1 = "hello"
# s2 = "world"
# Should return False
if not len(s1) == len(s2):
    print(False)
freq = dict()
for i in s1:
    freq[i] = freq.get(i, 0) + 1
for i in s2:
    freq[i] = freq.get(i, 0) - 1
for i in freq:
    if freq[i] < 0:
        print(False)
print(True)

# using 2 for loops
if not len(s1) == len(s2):
    print(False)
freq = dict()
for i in range(len(s1)):
    freq[s1[i]] = freq.get(s1[i], 0) + 1
    freq[s2[i]] = freq.get(s2[i], 0) - 1
for i in freq:
    if freq[i] < 0:
         print(False)
print(True)
