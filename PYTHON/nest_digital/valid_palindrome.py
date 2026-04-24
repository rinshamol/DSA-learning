def isPalindrome( s) -> bool:
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        if (clean == clean[::-1]):
            return True
        else:
            return False
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))