# Create tuple
from sre_constants import ANY


passenger = (12, True, 'Bonnell, Miss. Elizabeth', 'female', 58)

print(passenger)

# Accessing tuples
name = passenger[2]
age = passenger[-1]
survived_and_name = passenger[1:3]
gender_and_age = passenger[-2:]
is_female = 'female' in passenger
is_male = 'male' in passenger

print(name)
print(age)
print(survived_and_name)
print(gender_and_age)
print(survived_and_name, gender_and_age)
print(is_female, is_male)

# Unpacking tuples
def get_survival_info(passenger):
  (id, survived, name, gender, age) = passenger
  passenger = (age, gender, survived)
  return(passenger)
print(get_survival_info(passenger))


passenger = (11, True, "Sandstrom, Miss. Marguerite Rut", "female", 4)
print(get_survival_info(passenger))

passenger = (28, False, "Fortune, Mr. Charles Alexander", "male", 19)
print(get_survival_info(passenger))

passenger = (51, False, "Panula, Master. Juha Niilo", "male", 7)
print(get_survival_info(passenger))
