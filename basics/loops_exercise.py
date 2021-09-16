# Exercício 13: calcule o fatorial de um inteiro

n = 5
last = 1
amount = 1
while last <= n:
    amount *= last
    last += 1
print(amount)

# Multiplique os itens em uma lista por 10
ratings = [6, 8, 5, 9, 10]

filtered_ratings = []
for rating in ratings:
    filtered_ratings.append(rating * 10)
print(filtered_ratings)

# filtered_ratings = [rating * 10
#                     for rating in ratings
#                     ]
# print(filtered_ratings)

for rating in ratings:
    if rating % 3 == 0:
        print("Múltiplo de 3")
