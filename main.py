# Create a score variable from user input as an int
score = int(input("Enter your score (0-100): "))

grade = ""

# Set grade based on score
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is", grade)