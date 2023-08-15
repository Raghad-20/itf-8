def main():
    num_students = int(input("Enter the number of students: "))
    print()

    for student in range(1, num_students + 1):
        num_marks = int(input(f"Enter the number of marks for student {student}: "))
        marks = []

        for mark in range(1, num_marks + 1):
            mark_value = float(input(f"Enter mark {mark} for student {student}: "))
            marks.append(mark_value)

        average = sum(marks) / num_marks
        max_mark = max(marks)
        min_mark = min(marks)

        print(f"\nStudent {student} - Average: {average:.2f}, Max Mark: {max_mark}, Min Mark: {min_mark}\n")

main()
