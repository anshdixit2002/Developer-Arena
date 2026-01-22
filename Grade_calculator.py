Name = input("Enter student name: ")
Student_marks = int(input("Enter marks (0-100): "))
print("Enter marks from 0-100 only")  # Move inside validation later

if Student_marks >= 90:
    grade = "A"
    message = "Outstanding! Excellent work! 🎉"
elif Student_marks >= 80:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif Student_marks >= 70:
    grade = "C"
    message = "Good job! You can do better! 📈"
elif Student_marks >= 60:
    grade = "D"
    message = "Satisfactory. Study harder next time! 📚"
else:
    grade = "F"
    message = "Failed. Please work harder! 💪"

print(f"📊 RESULT FOR {Name.upper()}:")
print(f"Marks: {Student_marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
