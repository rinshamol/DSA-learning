def isAnagram(s, t):
    if len(s) != len(t):
        return 0
    frequency = {}
    for ch in s:
        frequency[ch] = frequency.get(ch,0)+1
    
    for ch in t:
        if ch in frequency:
            frequency[ch] -=1
        else:
            return 0
    for (key,value) in frequency.items():
        if(value != 0 ):
            return 0
    return 1


s = "listen"
t = "silent"
print(isAnagram(s,t))