str = "MADAME"
def isPalindrome(i):
    if(i>=len(str)/2) :
        return True
    if(str[i] != str[len(str)-i-1]) :
        return False
    return isPalindrome(i+1)
print(isPalindrome(0))
