# --- list --- (surround with [] brackets) ordered, changeable, duplicates
# motorcycle_brands = ["Honda","BMW" ,"Suzuki" ,"Kawasaki", "Ducati", "KTM", "Yamaha"]
# motorcycle_brands.append("SomethingElse")
# motorcycle_brands.remove("BMW")
# motorcycle_brands[0] = "null"
# motorcycle_brands.sort() # sort in alphabetical order
# motorcycle_brands.reverse() # reverse order
# # motorcycle_brands.clear() # clear index
# print(motorcycle_brands.index("Kawasaki")) # find index of an element returns error if there is no element in collection
# print(motorcycle_brands.count("KTM")) # retuns how many times an element is found in collection
# print(len(motorcycle_brands)) # returns length of collection
# print("Tristan" in motorcycle_brands) # returns boolean if element is in collection
# for motorcycle in motorcycle_brands:
#     print(motorcycle)

# --- set --- (surround with {} brackets) unordered, unchangeable, no duplicates
# foods = {"apple", "orange", "banana", "coconut"}
# foods.add("pineapple")
# foods.remove("banana")
# print(foods)
# # print(foods[0]) # (error) cannot use index with sets\

# --- tuple --- (surround with () brackets) ordered, unchangeable, duplicates
# foods = ("apple", "orange", "banana", "coconut")
# print(foods.index("apple"))
# print(len(foods))
# print("Orange" in foods)
# print(foods.count("apple"))