# Waf to print the length of a list list is parameter ;

cities=["pune","nashik","sambhjinagr","mumbai"]

def cal_len(list):
    length=(len(list))
    print(length)
    return length

cal_len(cities)
 
# WAF to print the element of a list in a single line ( list is the parameter)

def print_list(list):
     for item in list:
         print(item,end=" ")

print_list(cities)

# WAP to find the factorial of n ( n is the parameter )

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)    
    return fact

cal_fact(5)

#WAF to convert USD to inr

def usdTOinr(n):
    inr=n*88
    print(inr)
    return inr
usdTOinr(88)
                 
          