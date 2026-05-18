nums = [1, 3, 4, 2, 3, 7]

numSet = set()
for i in nums:
      if i in numSet:        
            print(True) 
      numSet.add(i)
print(False)  # don't forget this outside the loop!
