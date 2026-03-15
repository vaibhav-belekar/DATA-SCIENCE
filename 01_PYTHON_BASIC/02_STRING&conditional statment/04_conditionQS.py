#wap to check if a number enterd by the user is odd or even 

num=int(input("enter a number :"))

if(num%2==0):
    print(" number is even ")
else:
    print("number is odd")  
    
    
#wap to find the gratesr of 3 number enter by the user
a=int(input("enter a number a:"))
b=int(input("enter a number b:"))
c=int(input("enter a number c:"))   

if(a>b and a>c):
    print(a)
elif(b>c):
    print(b)  
else:
    print(c)    
    
    
#WAP to check if a number is multiple of 7 or not 

num=int(input("enter a number :"))

if(num%7==0):
    print("number is multiple of 7 ")  
else:
    print("number is not multiple of 7")     