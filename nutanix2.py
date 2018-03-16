def NutanixSequence(n,m):
    
    start_input = n
    result = n
    for i in range(0,m-1):
        result = compute_string(start_input)
        #print "result at ",i+1,result
        start_input = result
    return result
    
def compute_string(input):
        result = ""
        length = len(input)
        #print length
        i=0; j=0
        count = 0
        while(i<length):
            current_letter = input[i]
            #print "letter", current_letter
            while(j<length):
                if current_letter==input[j]:
                    #print "j",j
                    j+=1
                    count+=1
                else:
                    break
            result += current_letter+str(count)
            #print result
            count = 0
            if j<length:
                i=j
            else:
                break;
            #print i,j
        return result

n = raw_input().strip()
m = int(raw_input())

import datetime 
t1 = datetime.datetime.now()
result = NutanixSequence(n,m)
t2 = datetime.datetime.now()
print result
print t2-t1