def main(recipe, available):
    count = 0
    for ingredient in recipe:
        if ingredient not in available:
            return 0
    while True:
        for ingredient in recipe:
            available[ingredient] -= recipe[ingredient]
            if available[ingredient] < 0:
                return count
        count += 1

# UNKNOW=-1
# def solutuion(recipe, available):
#     amount = -1
#     for ingredient in recipe:
#         if ingredient in available:
#             ing_amount = available[ingredient]//recipe[ingredient]
#             if UNKNOW==amount or ing_amount < amount:
#                 amount = ing_amount
#         else:
#             return 0
#     return amount


# main({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})