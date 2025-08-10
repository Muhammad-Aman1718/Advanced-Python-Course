student: object = {
    "name": "Zain",
    "age": 20,
    "courses": ["web", "python", "Ai"],
    "roll#": 11,
}


# print(student.keys())
# print(student.values())
# print(student.copy())
# print(student["name"])
# print(student["courses"])
# student["favorite food"] = "Meat"


student2: object = {
    "name": "amna",
    "age": 30,
    "courses": ["web", "python", "Ai"],
    "roll#": 11,
}

student.update(
    {
        "name": "amna",
        "age": 30,
        "courses": ["web", "python", "Ai"],
        "roll#": 11,
    }
)


print(student)
