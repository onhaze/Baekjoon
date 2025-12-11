grade_list = [['A+', 4.5], ['A0', 4.0], ['B+', 3.5], ['B0', 3.0], ['C+', 2.5], ['C0', 2.0],['D+', 1.5], ['D0', 1.0],['F', 0.0]]

sum_credit = 0
sum_grade = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade == "P":
        pass
    else:
        sum_credit += credit
        for i in range(len(grade_list)):
            if grade_list[i][0] == grade:
                grade = float(grade_list[i][1])
                sum_grade += credit * grade

print(sum_grade / sum_credit)