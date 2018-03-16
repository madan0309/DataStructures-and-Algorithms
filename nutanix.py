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
        for i in xrange(0,length):
            if (i>=1 and input[i]==input[i-1]):
                continue
            count = 1
            current_letter = input[i]
            for j in range(i+1, length):
                if current_letter == input[j]:
                    count += 1
                else:
                    #print 'break',input[j]
                    break
            #print count, i
            result += current_letter+str(count)
            
        return result

n = raw_input().strip()
m = int(raw_input())
import datetime 
t1 = datetime.datetime.now()
result = NutanixSequence(n,m)
t2 = datetime.datetime.now()
print result
print t2-t1