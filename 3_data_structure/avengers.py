# collections

# 1 list
movies_avengers_list = ["Avengers", "Avengers 2", "Avengers 3"]
# 2 tuple. don't change values
movies_avengers_tuple = ("Avengers", "Avengers 2", "Avengers 3", "Avengers 4")
# 3 sets. Don't support indexation
movies_avengers_sets = {"Avengers", "Avengers 2", "Avengers 3"}
# 4 dictionary, key value
moviesAvengers = {"Avengers 1": "The Avengers", "Avengers 2": "Ultron", "Avengers 3": "Infinity War",
                  "Avengers 4": "End Game"}

# show one element
print(movies_avengers_list[0])  # 1
print(movies_avengers_tuple[0])  # 2
# 3 x
print(moviesAvengers["Avengers 1"])  # 4

# add
movies_avengers_list.append("Avengers 4")  # 1
# 2 x
movies_avengers_sets.add("Avengers 4")  # 3
moviesAvengers.setdefault("Avengers 4", "End Game")  # 4

# remove
movies_avengers_list.pop(2)  # 1
# 2 x
movies_avengers_sets.remove("Avengers 3")  # 3
moviesAvengers.pop("Avengers 3")  # 4

# show all elements

print("list")

for tech in movies_avengers_list:
    print(tech)

print("tuple")

for tech in movies_avengers_tuple:
    print(tech)

print("sets")

for tech in movies_avengers_sets:
    print(tech)

print("dictionary")
for tech in moviesAvengers:
    print(tech)

# len
len(movies_avengers_list)
len(movies_avengers_tuple)
len(movies_avengers_sets)
len(moviesAvengers)
