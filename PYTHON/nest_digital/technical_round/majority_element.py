def majorityElement(A):
        if not A:
            return -1
        n = len(A)
        freq = {}
        for i in A:
           freq[i] = freq.get(i,0)+1
          
        majority = n/2
        for i,f in freq.items():
            print(f)
            if f >= majority:
                return i
        return -1
print(majorityElement([2,1,2]))