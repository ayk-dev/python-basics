n = int(input()) # number of people in jury

presentation_counter = 0

presentaion = input()

all_presentations_grades = 0

while presentaion != 'Finish':
    total = 0
    for pres in range(1, n + 1):
        grade = float(input())
        total += grade
    average_grade = total / n
    all_presentations_grades += average_grade
    print(f'{presentaion} - {average_grade:.2f}.')

    presentaion = input()
    presentation_counter += 1


final_average = all_presentations_grades / presentation_counter
print(f"Student's final assessment is {final_average:.2f}.")


