n=3 
def generateBrackets(n):
    result = []
    def backTracking(current,open_count,close_count):
        if(len(current) == 2*n):
            result.append(current)
            return
        if open_count < n :
            backTracking(current + '<', open_count + 1, close_count)
        if close_count < open_count :
            backTracking(current +'>',open_count, close_count+1)
    backTracking("",0,0)
    return result
print(generateBrackets(n))