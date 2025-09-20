#string operation

#concatantion
print("\nstring concatanation example ~")

str1="vaibhav"
str2="belekar"

finalstr=str1+' '+str2

print(finalstr)

#find length of sting 
print("\nlength example ~")

print(len(str1))
print(len(finalstr))

#indexing in python
print("\nindexing examples ~")
str="vaibhav_belekar"
ch=str[0]

print(ch)

# string slicing example ~
print("\nstring sclicing example ~")

name="vaibhavBelekar"
print(name[1:4])
print(name[:4])
print(name[0:])

print(name[-5:-1]) # negative index

#string function
print("\nstring oepration exampple")

str="i am learning python"
print(str.endswith("n"))
print(str.capitalize())
print(str.replace("python","java"))
print(str.find("python"))
print(str.count("am"))

""" outputs :~ 
string concatanation example ~
vaibhav belekar

length example ~
7
15

indexing examples ~
v

string sclicing example ~
aib
vaib
vaibhavBelekar
leka

string oepration exampple
True
I am learning python
i am learning java
14
1


"""

