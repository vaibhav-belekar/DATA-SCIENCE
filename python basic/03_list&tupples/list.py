# lecture 3 list & tuples 

marks =[85,55,66,44,55,88]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

student=["vibhav",85,"sambhajinagr"]
print(student)

student[0]="belekar"
print(student)

#list slicing 
print(marks[0:4])
print(marks[ :len(marks)])
print(marks[-3:len(marks)])

# methods in list 
print("\nexample of list : ~")
list=[2,1,3]

list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(1,5)
print(list)

list.remove(1)
print(list)

list.pop(2)
print(list) 