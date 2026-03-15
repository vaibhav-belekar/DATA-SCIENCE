#WAP to ask the user to enter names of their 3 favourite movies & stire them in a list 
movies=[]
movies.append(input("enter the 1 movies:"))
movies.append(input("enter the 1 movies:"))
movies.append(input("enter the 1 movies:"))

print(movies)

#wap  to check if a list contain a palindrome of element (hint use copy()method )

list1=[1,2,3,4,3,2,1]
copy_list=list1.copy()
copy_list.reverse()

if(copy_list==list1):
    print("palindrome")
else:
    print(" not palindrome")     