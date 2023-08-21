total = 0
student_count = int(input("Enter Student Count: "))
for j in range(student_count):
    marks_count = int(input("Enter Marks Count: "))
    my_marks = []
    for i in range(0, marks_count):
        mark = float(input(f"Enter mark {i+1}: "))
        my_marks.append(mark)

    average = sum(my_marks) / len(my_marks)
    print(average)
    print(my_marks)

    print(f"Max Mark = {max(my_marks)}")
    print(f"Min Mark = {min(my_marks)}")