# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

# student_data =  namedtuple('student_data', 'ID, MARKS, CLASS, NAME')

n = int(input())
student = namedtuple("Student", input().split())

mark_total = 0

for i in range(n):
    student_data = input().split()
    students = student(*student_data)
    mark_total += int(students.MARKS)

print(mark_total / n)
# column_name = [list(input().split())]
# for n in range(N):
#     for column in column_name:
