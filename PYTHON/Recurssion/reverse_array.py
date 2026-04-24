arr = [2,3,4,5]

def swap(l,r):
    if(l>=r): 
        return
    arr[l],arr[r] = arr[r],arr[l]
    swap(l+1,r-1)
    
swap(0,len(arr)-1)
print(arr)