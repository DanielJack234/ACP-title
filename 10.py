#........ Recipe Explorer .......

# STEP 1 - Create for recipe details (fixed - cannot be changed)
pasta = ("Pasta Arrabiata", "Italian",  20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

# STEP 2 - Nested tuples and slicing 
all_recipes = (pasta, biryani)
print("/nFirst Recipe Name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "minutes")
print("Pasta details (sliced):", pasta[1:3])

# STEP 3 - Iterate through a tuple 
print("/nPasta Recipe details:")
for detail in pasta:
    print("-", detail)

# STEP 4
pasta_ingredients = {"tomato", "garlic", "olive oil", "chili", "pasta", "garlic"}
biryani_ingredients = {"chicken", "rice", "yogurt", "spices", "onion", "garlic"}
print("/nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))

#STEP 5
pasta_ingredients.add("parmesan")
pasta_ingredients.remove("chili")
print("/nUpdated Pasta Ingredients:", pasta_ingredients)

# STEP 6
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("/nAll Ingredients:", all_ingredients)
print("Common Ingredients:", common)
print("Ingredients only in Pasta:", only_pasta)
print("Not shared (sym. difference):", unique_to_each)
