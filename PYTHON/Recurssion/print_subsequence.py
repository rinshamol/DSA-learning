arr = [3,1,2]
def subsequence(index,sub):
	if(index >=  len(arr)) :
		print(sub)
		return
	sub.append(arr[index])
	subsequence(index+1,sub)
	sub.remove(arr[index])
	subsequence(index+1,sub)

	
subsequence(0,[])