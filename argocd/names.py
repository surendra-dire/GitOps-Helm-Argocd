name=[
{
"name": "Alice",
"age": 25,
"is_student": True,
"courses": ["Math", "Physics", "Computer Science"],
"address": {
"city": "Wonderland",
"zipcode": "12345"
}
},
{
"name": "Bob",
"age": 30,
"is_student": False,
"courses": ["History", "Philosophy"],
"address": {
"city": "Riverdale",
"zipcode": "67890"
}
},
{
"name": "Charlie",
"age": 22,
"is_student": True,
"courses": ["Biology", "Chemistry", "English"],
"address": {
"city": "Metropolis",
"zipcode": "54321"
}
}
]
display_dict={}
for index,key in enumerate(name):
    print (key,index)


# expected output
# Name: Alice, Age: 25, City: Wonderland
# Name: Bob, Age: 30, City: Riverdale
# Name: Charlie, Age: 22, City: Metropolis