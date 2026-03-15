tup=(1,2,3,4,5,5,7)

for num in tup:
    print(num)


str="vaibhav belekar"
for char in str:
    print(char)
else:
    print("end") 
    
#Q1) print the element of the following list using a loop

sqr=[1,4,9,16,25,36,49,64,81,100]

for nums in sqr:
    print(nums)

#Q2) search for a number x in this using loop
sqr=[1,4,9,16,25,36,49,64,81,100]
x=36

idx=0
for nums in sqr:
    if(nums==x):
        print("number find at index ",idx)
    idx+=1
#for range function

for el in range(5):
    print(el)
for el in range(1,5):# range start and end
    print(el)
for el in range(1,10,2):# range(start,stop,step)
    print(el)             