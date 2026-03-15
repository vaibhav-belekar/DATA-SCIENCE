# # Q1)  print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1
    
    
    
# #Q2) print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
    
# #Q2) print the multiplication table of a number n
#     n=int(input("enter the number n"))
#     i=1
    
#     while i<10:
#         print(n*i)
#         i+=1
        
        
        
#Q4)print the elemet of the following list using a loop       
        
# nums=[1,4,9,16,25,36,49,64,81,100]   

# idx=0   
# while idx<len(nums):
#     print(nums[idx]) 
#     idx+=1
    
# # search for a number x in this tuple using loop
# tup=(1,4,9,16,25,36,49,64,81,100) 
# x=36

# i=0
# while i<len(tup):
#     if(tup[i]==x):
#         print("found at idx ",i) 
#         break
#     else:
#         print()    
#     i+=1


# use of break keyword
i=1
while i<=100:
    print(i)
    if(i==3):
        break
    i+=1
            