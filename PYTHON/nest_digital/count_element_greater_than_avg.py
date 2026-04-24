def countResponseTimeRegressions(responseTimes):
    count = 0
    sum = 0
    for i in range(1,len(responseTimes)):
        sum += responseTimes[i-1]
        avg = sum/i
        if avg < responseTimes[i]:
            count += 1
    return count
print(countResponseTimeRegressions([100, 200, 150,300]))