# just use for, lists, conditional

student_scores = [150,234,160,345,133,177,723,733,572,634,237,784,574]

# print(max(student_scores))

temp_max = 0
for score in student_scores:
    if temp_max < score:
        temp_max = score
print(temp_max)