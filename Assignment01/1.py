student_grades: dict[str,int] = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78
}

def get_grade(name):
    return student_grades.get(name, "Not Found")

print(get_grade("Alice"))
print(get_grade("Bob"))
print(get_grade("Achu"))
