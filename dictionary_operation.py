student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}

print("Initial student record:")
for key, value in student.items():
    print(f"{key}: {value}")
print()

if "email" not in student:
    email = input("Please enter an email: ").strip()
    student["email"] = email

while True:
    new_city = input("Please enter a new city: ").strip()
    if new_city:
        student["city"] = new_city
        break
    print("City cannot be empty.")

phone = student.get("phone")
if phone is None:
    print("Phone number not found.")
    phone = input("Please enter a phone number: ").strip()

student["contact"] = {
    "phone": phone,
    "email": student["email"]
}

student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

def calculate_average(courses):
    total = 0
    count = 0
    for score in courses.values():
        total += score
        count += 1
    return total / count if count > 0 else 0

def get_academic_status(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 60:
        return "Pass"
    else:
        return "At Risk"

average = calculate_average(student["courses"])
student["academic_status"] = get_academic_status(average)

search_course = input("Enter a course name to search: ").strip()
if search_course in student["courses"]:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found")

update_course = input("Enter a course name to update: ").strip()

while True:
    try:
        new_score = float(input(f"Enter new score for {update_course} (0-100): "))
        if 0 <= new_score <= 100:
            if new_score.is_integer():
                new_score = int(new_score)
            break
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

if update_course in student["courses"]:
    old_score = student["courses"][update_course]
    student["courses"][update_course] = new_score
    print(f"{update_course} score updated from {old_score} to {new_score}.")
else:
    student["courses"][update_course] = new_score
    print(f"New course {update_course} added with score {new_score}.")

average = calculate_average(student["courses"])
student["academic_status"] = get_academic_status(average)

print()
print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print()
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print()
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print()
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score}")
print()
print(f"Average Score: {average:.1f}")
print(f"Academic Status: {student['academic_status']}")
print()
print("=====================================")
