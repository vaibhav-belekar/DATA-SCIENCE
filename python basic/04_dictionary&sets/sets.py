# sets in python 
collection={1,2,3,4,5,"vaibhav","belekar"} #repeted element store only ones
print(collection)
print(type(collection))

collection={}
print(type(collection))

collection=set()#empty set; syntax
print(type(collection))

# methods 
print(" this are the method ~")
collection.add(88)
collection.add(5)
collection.add(8)
print(collection)

collection.remove(88)
print(collection)

collection.pop()

collection.clear()
print(collection)

#union and intersection in sets 

set1={1,2,3,4}
set2={2,5,4,8}

print(set1.union(set2))
print(set1.intersection(set2))



