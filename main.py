
# PLACEMENT READINESS TRACKER
# IRP-II Assignment - Task 1, Task 2 and Task 3

# ==========================================
# TASK 1: DATA AND CONTROL STRUCTURES
# ==========================================

students = [
    {"name": "Rahul", "roll_no": 101, "aptitude": 85, "verbal": 78, "coding": 90},
    {"name": "Priya", "roll_no": 102, "aptitude": 75, "verbal": 88, "coding": 82},
    {"name": "Aman", "roll_no": 103, "aptitude": 60, "verbal": 65, "coding": 70},
    {"name": "Neha", "roll_no": 104, "aptitude": 92, "verbal": 90, "coding": 95},
    {"name": "Karan", "roll_no": 105, "aptitude": 45, "verbal": 55, "coding": 50}
]


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def get_score(subject):
    while True:
        score = get_integer(f"Enter {subject} score (0-100): ")

        if 0 <= score <= 100:
            return score
        print("Invalid score! Enter a value between 0 and 100.")


print("===== ADD NEW STUDENT =====")

name = input("Enter student name: ")
roll_no = get_integer("Enter roll number: ")

new_student = {
    "name": name,
    "roll_no": roll_no,
    "aptitude": get_score("Aptitude"),
    "verbal": get_score("Verbal"),
    "coding": get_score("Coding")
}

students.append(new_student)

print("\nStudent added successfully!")


# ==========================================
# TASK 2: FUNCTIONS
# ==========================================

def average(student):
    return (
        student["aptitude"]
        + student["verbal"]
        + student["coding"]
    ) / 3


def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


def top_scorer(students):
    return max(students, key=average)


def needs_practice(students, limit=40):
    return [s for s in students if average(s) < limit]


print("\n========== PLACEMENT READINESS REPORT ==========")
print(f"{'Name':<12}{'Roll No':<10}{'Average':<12}{'Grade'}")
print("-" * 48)

for student in students:
    avg = average(student)
    print(
        f"{student['name']:<12}"
        f"{student['roll_no']:<10}"
        f"{avg:<12.2f}"
        f"{grade(avg)}"
    )

best_student = top_scorer(students)

print("\nTop Scorer:", best_student["name"])
print("Highest Average:", round(average(best_student), 2))

practice_students = needs_practice(students)

print("\nStudents Needing Extra Practice:")

if practice_students:
    for student in practice_students:
        print(student["name"], "-", round(average(student), 2))
else:
    print("No students need extra practice.")


# ==========================================
# TASK 3: RUNNER-UP SCORE
# ==========================================

print("\n========== RUNNER-UP SCORE PROBLEM ==========")

n = get_integer("Enter number of scores: ")

while n < 2 or n > 100:
    print("Enter n between 2 and 100.")
    n = get_integer("Enter number of scores: ")

scores = []

for i in range(n):
    score = get_integer(f"Enter score {i + 1}: ")

    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = get_integer(f"Enter score {i + 1}: ")

    scores.append(score)

distinct_scores = sorted(set(scores), reverse=True)

if len(distinct_scores) >= 2:
    print("Runner-up Score:", distinct_scores[1])
else:
    print("At least two distinct scores are required.")
