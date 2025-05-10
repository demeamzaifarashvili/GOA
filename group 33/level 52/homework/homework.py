#1
def cakes(recipe, available):
    return min(available.get(ingredient, 0) // amount for ingredient, amount in recipe.items())

#2
def alphanumeric(password):
    return password.isalnum()

#3?

#4?