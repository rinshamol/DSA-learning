intervals = [[1, 3], [11, 6], [8, 10], [15, 18]]
def mergeHighDefinitionIntervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals :
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1],interval[1])
    return merged
    


print(mergeHighDefinitionIntervals(intervals))