student = {
    "name": "Gertrude",
    "age": 20,  
    "adm": "12345",
    "courses": ["Math", "Science", "History"],
    "grades": {
        "Math": 85,
        "Science": 90,
        "History": 78
    }
}
print(type(student))
print(student["name"])
print(student["courses"][1])
print(student["grades"]["Science"])
# updating
student["age"]=21
print(student["age"])
# adding
student["gender"]="Male"
print(student)
#Deleting
del (student["age"])
print(student)
# .get()
print(student.get("name"))
# .keys()
print(student.keys())
# .values()
print(student.values())
# .items() displays the key-value pairs in the dictionary as tuples in a list
print(student.items())
# .pop() removes the specified key and returns the corresponding value
removed_value = student.pop("adm")
print(removed_value)
print(student)
# .popitem() removes the last inserted key-value pair from the dictionary and returns it as a tuple
removed_item = student.popitem()
print(removed_item)