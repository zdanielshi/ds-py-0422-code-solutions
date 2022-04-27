# Loop Tuples
record = (1, "Grimdiana", "Bones", "boulders")

row = ''

for x in record:
  print(x)
  row = row + str(x) + ", "

print(row)

# Loop Lists
values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

for x in values_list:
  print(x)

index_list = []

for i in range(len(values_list)):
  print(i)
  index_list.insert(0, i)

print(index_list)

for i in index_list:
  if i % 2 != 0:
    values_list.pop(i)

print(values_list)

# Loop Sets
vowels = {"A", "E", "I", "O", "U"}
parts_of_the_big_letter = {"L", "M", "N", "O", "P"}

for i in vowels:
  parts_of_the_big_letter.discard(i)

print(parts_of_the_big_letter)

# Loop dictionary
player_positions = {
    "Who": "1B",
    "What": "2B",
    "I Don't Know": "3B",
    "Why": "LF",
    "Because": "CF",
    "Tomorrow": "P",
    "Today": "C",
    "I Don't Care": "SS"
    }

players = []

for x in player_positions:
  players.insert(0, x)

print(players)

positions = []

for x in player_positions.values():
  positions.insert(0, x)

print(positions)

for x, y in player_positions.items():
  print(x, " is on ", y)
