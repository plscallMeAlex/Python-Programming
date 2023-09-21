def grade_compare(sc):
    if 80 <= sc <= 100:
        return "A"
    elif 70 <= sc < 80:
        return "B"
    elif 60 <= sc < 70:
        return "C"
    elif 50 <= sc < 60:
        return "D"
    elif 0 <= sc < 50:
        return "F"
    else: 
        return "Invalid"

score = int(input("Enter Your Score: "))
print(f"Your grade is: {grade_compare(score)}")