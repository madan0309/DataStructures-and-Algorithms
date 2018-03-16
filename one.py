import itertools

def solution(S):
    # write your code in Python 3.6
    Input = S[:2]+S[3:]
    all_perms = itertools.permutations(Input)
    min = 9999
    min_time = ""
    for time in set(all_perms):
        
        #print time
        computed_time1 = int(time[0])*10 + int(time[1])
        computed_time2 = int(time[2])*10 + int(time[3])
        if (computed_time1>24) or (computed_time2>59):
            continue
        else:
            time_diff1 = computed_time1 - int(S[:2])
            if time_diff1 <0:
                time_diff1 += 24
            time_diff2 = computed_time2 - int(S[3:])
            if time_diff2 < 0:
                time_diff2 +=60
                time_diff1 -= 1
                if time_diff1 < 0:
                    time_diff1 += 24
            time_diff = time_diff1*100 + time_diff2
            #print time_diff1, time_diff2, time_diff
            if time_diff <= 0:
                continue
            if time_diff < min:
                min = time_diff
                min_time = time
    if min==9999:
        return S
    else:
        #print min
        return min_time[0]+min_time[1]+":"+min_time[2]+min_time[3]
    
s = raw_input()
print "Anser", solution(s)