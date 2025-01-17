# Task
# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.
#
# The format for the general mark sheet is:
#
# Student ID → ___1_____2_____3_____4_____5__
# Subject 1   |  89    90    78    93    80
# Subject 2   |  90    91    85    88    86
# Subject 3   |  91    92    83    89    90.5
#             |______________________________
# Average        90    91    82    90    85.5

if __name__ == '__main__':
    n_student, x_subjects = map(int, input().split())

    marks = []
    for _ in range(x_subjects):
        students_marks = tuple(map(float, input().split()))
        marks.append(students_marks)

    zipped_scores = zip(*marks)

    for score in zipped_scores:
        average = sum(score) / x_subjects
        print(average)
