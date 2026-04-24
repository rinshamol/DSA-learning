def isNonTrivialRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return False
    s1s1 = s1+s1
    if s2 in s1s1:
        return True
    return False
s1 = "abcde"
s2 = "cdeab"
print(isNonTrivialRotation(s1,s2))