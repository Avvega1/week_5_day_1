#######sets#########
# sets are unordered and unindexed 
# they are defined using curly brackets 
# they do not allow duplicates
fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
print(fruits)
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("volvo" in fruits)
print(fruits.add("orange"))
print(fruits)
print(fruits.add("kiwi"))
print(fruits)

print(fruits.update(["orange", "kiwi", "pineapple"]))
print(fruits)

print(fruits.remove("banana"))
print(fruits)
print(fruits.pop())
print(fruits)
print(fruits.clear())
print(fruits)


social_security_numbers = {123456789, 987654321, 123456789}

# print(social_security_numbers.pop())
print(social_security_numbers)
print(social_security_numbers.add(345678901))
print(social_security_numbers)
social_security_numbers.add(123456789)
print(social_security_numbers)

#######tuples#########

example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(example_tuple)
# print(example_tuple.count(2))

# print(dir(example_tuple))
# print(help(example_tuple))
# print(len(example_tuple))
# print(2 in example_tuple)
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers"
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# print(lymeric_tuple.count("p"))

#loops with tuples
for item in example_tuple:
    print(item)


#dictionary
capitals = {"kenya" : "nairobi",
            "uganda" : "kampala",
             " tanzania" : "dodoma",
             "rwanda" : "kigali",
             "china" : "beijing",
             "USA" : " washington dc"}
print(capitals)
print(dir(capitals))
print(help(capitals))
print(len(capitals))
print(capitals["kenya"])
print(capitals.get("kenya"))
capitals["south africa"] = "pretoria"
print(capitals)
capitals.update({"nigeria":"abuja"})
capitals.update({"france":"paris", "germany":"berlin", "italy":"rome"})

for key in capitals : 
    print(f"these are the {key}")

for value in capitals.values():
    print(value)

items_all = capitals.items()
for key, value in items_all:
    print(f"{key} is the capital of {value}")