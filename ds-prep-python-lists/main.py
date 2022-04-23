ages = [29, 19, 17, 26, 32, 16, 21]
print(ages)

#Accessing List Items
## printing 5th element
print(ages[4])

## printing second-to-last element
print(ages[-2])

## print 3rd to sixth elements
print(ages[2:6])

## print first four elements
print(ages[:4])

## check if 17 is in list
print(17 in ages)

## check if 42 is in the list
print(42 in ages)

# Changing List Items
## changing 3rd value to 18
ages[2] = 18
print(ages)

## swapping 4th and 5th values
temp = ages[4]
ages[4] = ages[3]
ages[3] = temp
print(ages)

#Adding list items
# appending 45 to back of the list
ages.append(45)
print(ages)

# insert 32 to the front of the list
ages.insert(0, 32)
print(ages)

# insert 37 before the 6th value of the list
ages.insert(5,37)
print(ages)

#Removing list items
#remove the last value
ages.pop()
print(ages)

# remove the 3rd value
ages.pop(2)
print(ages)
