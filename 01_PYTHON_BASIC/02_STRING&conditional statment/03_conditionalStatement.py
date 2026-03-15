 # example of conditional statement

light="pink"

if(light=="red"):
    print("wait")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

else:
    print("light is broken")
    
print("end of the code")                


# for grade system
marks= int(input("enter your marks :"))

if(marks>=90):
    grade="A"

elif(marks>=80 and marks<90):
    grade="B"
    
elif(marks>=70 and marks<80):
    grade="C"
            
else:
    grade="D" 

print("your grade is ",grade )               

#nesting in python
age=95

if(age>=18):
    if(age>=90):
        print("you cant drive")
    else:
        print("you can drive")    

else:
    print("you cant drive ")        