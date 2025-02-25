"""Examples of the tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences so they're 0-indexed
print(goat[0])
print(goat[1])

# Printing a tuple produces its literal syntax
print(goat)

# print both items on the same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for..in loops
# Meaning you can loop over thm
for item in goat:
    print(item)

# Typles, unlikes lists, are immutable
# Which means we cannot reassing items, nor append, nor pop, etc.
# goat[0] = "LBJ"

# We can "invent" our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create varibles of that type
unc_poy: Player = ("Bacot", 5)

# in a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)



# A range is another common sequnce tpye
zero_to_nine: range = range(0, 10, 1)

# we can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# we can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["Jeeya", "Ritika", "Dhruti", "Ritesh"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


# Range that is specifying the indices that you want printed
for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")


print(odds_to_99.stop)