def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key = lambda x: x[1])
    non_overlaped = []
    for interval in meetings:
        if not non_overlaped or non_overlaped[-1][1] <= interval[0]:
            non_overlaped.append(interval)
    return len(non_overlaped) 
meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(maximizeNonOverlappingMeetings(meetings))