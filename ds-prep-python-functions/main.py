# boolean to integer
from cmath import pi


bool_to_int = lambda value : int(value)

print(bool_to_int(True))
print(bool_to_int(False))

# get smaller value
get_smaller = lambda a, b : min(a, b)

print(get_smaller(16,31))
print(get_smaller(253, 223))

# cubing
def cube(base):
  return base ** 3

print(cube(2))
print(cube(5))

# absolute difference between values
def absolute_difference(a, b):
  difference = a - b
  return abs(difference)

print(absolute_difference(14, 11))
print(absolute_difference(13,40))

# squared difference
def squared_difference(a, b):
  difference_to_square = a - b
  return difference_to_square ** 2

print(squared_difference(14, 11))
print(squared_difference(13, 40))

# hours to minutes
def hours_to_minutes(hours):
  return hours * 60.0

print(hours_to_minutes(hours = 3.5))
print(hours_to_minutes(hours = 12))

# getting the circumference
def get_circumference(radius):
  return radius * 2 * pi

print(get_circumference(radius = 1))
print(get_circumference(radius = 9.2))

# linear transformation
def linear_transform(x, slope, intercept):
  return x * slope + intercept

print(linear_transform(x = 5.0, slope = 3.0, intercept = -8.5))
print(linear_transform(slope = -2.1, intercept = 17.0, x = 2.5))

# standardize
def standardize(x, x_center, scale_size):
  return (x - x_center) / abs(scale_size)

print(standardize(x = 8.2, x_center = 13.8, scale_size = 4.83))
print(standardize(scale_size = 24.63, x = 2.89, x_center = -72.813))
