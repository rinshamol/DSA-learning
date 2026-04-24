def isAlphabeticPalindrome(code):
    alpha = ''.join(ch.lower() for ch in code if ch.isalpha())
    left = 0
    right = len(alpha)-1
    while left < right:
        if(alpha[left] != alpha[right]):
            return 0
        else:
            left += 1
            right -= 1
    return 1
code = "A1b2B!a"
print(isAlphabeticPalindrome(code))