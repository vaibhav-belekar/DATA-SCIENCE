#store following word meaning in a python  dictionary

dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of fact & figures"]

}

print(dictionary)


#q3
marks={}

x=int(input("enter the phy marks :"))
marks.update({"phy":x})

x=int(input("enter the math marks :"))
marks.update({"math":x})

x=int(input("enter the chem marks :"))
marks.update({"chem":x})

x=int(input("enter the math marks :"))
marks.update({"eng":x})

print(marks)
 
# Q4 figure out a way  to store 9 & 9.0 as seperate values in the set 

values={
    ("float",9.0),
    ("int",9)
}

print(values)