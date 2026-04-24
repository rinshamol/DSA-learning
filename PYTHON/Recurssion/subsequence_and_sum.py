arr = [1,2,1,2]
sum = 2

def subsequence(index,sub,s) :
    if(index >= len(arr)) :
        if(sum == s):
            print(sub)
        return
    
    sub.append(arr[index])
    s +=arr[index]
    subsequence(index+1,sub,s)
    sub.remove(arr[index])
    s -= arr[index]
    subsequence(index+1, sub, s)
print("All Subsequences with sum 2 are :")
subsequence(0,[],0)

def singleSubsequence(index, sub,s):
    if(index >= len(arr)) :
        if(sum == s):
            print(sub)
            return True
        return False
    sub.append(arr[index])
    s += arr[index]
    if(singleSubsequence(index + 1,sub,s) == True):
        return True
    sub.remove(arr[index])
    s -= arr[index]
    if(singleSubsequence(index + 1,sub,s) == True):
        return True
    

print("Is there any subsequence with sum 2 ?")
singleSubsequence(0,[],0)

def countSubsequence(index,s):
    if(index >= len(arr)) :
        if(sum == s) :
            return 1
        return 0
    s += arr[index]
    l = countSubsequence(index + 1, s)
    s -= arr[index]
    r = countSubsequence(index + 1, s)
    return l + r
print("Total number of subsequences with sum 2 are :")
print(countSubsequence(0,0))