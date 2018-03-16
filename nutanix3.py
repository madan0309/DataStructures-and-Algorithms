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
        count = 1
        for i in range(length):
            if (i !=length-1 and input[i+1]==input[i]):
                count+=1
            else:
                result += input[i] + str(count)
                #print "res ",result
                count = 1
        return result

n = raw_input().strip()
m = int(raw_input())
import datetime 
t1 = datetime.datetime.now()
result = NutanixSequence(n,m)
t2 = datetime.datetime.now()
print result
print t2-t1