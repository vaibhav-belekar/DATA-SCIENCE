#learning dictionary

info={
    "name":"vaibhav",
    "age":29,
    "address":"lakhani",
    "grade":"A"
}

print(info)
info["name"]="vaibhav Belekar"
print("after assign new value",info)

# nested dictonary
student={
    "name":"vaibhav belekar",
    "subjects":{
        "chem":97,
        "math":85,
        "english":98
    }
}

print(student)
print(student["subjects"]["chem"])


#method
student.keys() #return all keys 
student.values()#return all values
student.items()#return all (key, val)pairs as tuple 
student.get("subjects")#return the key according to tuple
student.update()#add the specific item to the dictonry