day_of_week = 'saturday'


if day_of_week == 'saturday' or day_of_week == 'sunday':
  print('Have a good weekend!')
else:
  print("It's a weekday!")

# Student 1 score
student_1_score = 47

if student_1_score >= 70:
  pass_or_fail = "You passed!"
else:
  pass_or_fail = "You failed!"

print(student_1_score)
print(pass_or_fail)

#Student 2 score
student_2_score = 87

if student_2_score >= 100:
  letter_grade = 'A+'
elif student_2_score >= 90:
  letter_grade = 'A'
elif student_2_score >= 80:
  letter_grade = 'B'
elif student_2_score >= 70:
  letter_grade = 'C'
elif student_2_score >= 60:
  letter_grade = 'D'
else:
  letter_grade = 'F'

print(student_2_score)
print(letter_grade)

# Seasons
def get_season_info(value):
  if value == 'summer':
    return "Statistically, it's likely to be hotter today than in 6 months from now. Don't sweat it, though."
  elif value == 'spring':
    return "The flowers are blooming while it's spring, but that correlation, not causation."
  elif value == 'autumn':
    return "The leaves seem to regress to warmer colors as autumn approaches its end."
  elif value == 'winter':
    return "There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater."
  else:
    return" That's not a season. Most likely."

print(get_season_info('summer'))
print(get_season_info('spring'))
print(get_season_info('autumn'))
print(get_season_info('winter'))
print(get_season_info('other'))

# Age
age = 42

print('adult') if age >= 18 else print('child')
