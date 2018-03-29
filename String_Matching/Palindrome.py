"""
Longest palindrome substring in given text
"""

def max_polindrome(input): #input- text output-max_lengh(polindrome)
    n = len(input)
    max_poli = 1
    for i in range(0, n):
        poli = 1
        if(i !=(n-1)):
            #check for even length polindrome
            #check for 0 index
            if(input[i]==input[i+1] and i!=0):
                poli = 2
                low = i-1
                high = i+2
            else:
                low = i-1
                high = i+1
            while(low>=0 and high<n):
                if input[low]==input[high]:
                    poli+=2
                else:
                    break
                low-=1
                high+=1
            if (poli>max_poli):
                max_poli = poli
    return max_poli
input = "dacbhhgghhbcahabbahe"
print max_polindrome(input)