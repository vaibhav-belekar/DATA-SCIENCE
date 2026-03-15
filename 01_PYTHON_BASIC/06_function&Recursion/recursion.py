#recursion

def show(n):
    if(n==0):  #base case
        return
    print(n)
    show(n-1)

show(10) 

#factorial using recursiion

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fact(10))

#lets Practice 

# write a recursive to calculate the sum of first n natural number 
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)

#write a recursive function to print all elemet in a list hint use list and index as a parameter

def print_element(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_element(list,idx+1)
fruits=["apple","banana","cherry","orange"]    
print_element(fruits)    
    
    