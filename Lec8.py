'''
Function
'''

def cal_plus(input1,input2):
    return input1+input2
    
    result= input1+input2
    return result
    
print(cal_plus(1,3))
print(cal_plus(2,7))

#print(cal_plus(input2=1,input1=3))
print(cal_plus(2,7))
#print(cal_plus(2))
#print(input1) does not work

def cal_abs(a):
    
    if type(a) is str:
        return()
        
def calculate_abs(a):
    if type(a) is str:
   #     return: ('wrong data type')
        
    #elif: a>=0:
        return a
    else:
        return -a
print(cal_abs(468))

def cal_sigma(m,n):
    result=0
    for i in range (n,m+1):
        result=result+i
        #n+ n+1 + n+22... 
        
    return(result)

print(cal_signma(10,3))

def cal_f(m):
    if m==0:
        return 1
    else:
        return m * cal_f(m-1)

# print (cal_f(5))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)

print(cal_p(5,3))
