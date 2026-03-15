# f = open(r"C:\\Users\\Hp\\OneDrive\\Desktop\\data science\\DATA-SCIENCE\\python basic\\file IO\\demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))

# line1=f.readline()
# print(line1)
# f.close()

f=open("demo.txt","a") 
f.write("\nwe used now append mode to write ") 
f.close()


with open("demo.txt","r") as f:
    data=f.read()
    print(data)

# module
import os

os.remove(r"C:\\Users\\Hp\\OneDrive\\Desktop\\data science\\DATA-SCIENCE\\python basic\\file IO\\demo.txt")