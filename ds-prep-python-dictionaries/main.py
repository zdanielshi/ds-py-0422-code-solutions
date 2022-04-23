# create dictionary
person = {
  "first_name": "Leto",
  "last_name": "Atreides",
  "hobby": "travel"
}

print(person)

# Accessing items
## square bracket method
first_name = person['first_name']
print(first_name)

## get method
last_name = person.get('last_name')
print(last_name)

## get non-existent middle name
middle_name = person.get('middle_name')
print(middle_name)

## first, middle, last name
print(first_name, middle_name, last_name)

# Adding items
person['job'] = 'Duke'
print(person['job'])

# Changing dictionary values
person['hobby'] = 'cooking'
print(person['hobby'])

# Removing item from dictionary
person.pop('last_name')
print(person)
