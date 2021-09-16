## Estruturas de repetição

### Tipo tradicional
```python
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# Em alguns casos, ainda podemos querer percorrer uma sequência numérica, e para isto iteramos sobre a estrutura de dados range
for index in range(5):
    print(index)
```

Várias outras estruturas são iteráveis, como strings ( str ), tuplas ( tuple ), conjuntos ( set ), dicionários ( dict ) e até mesmo arquivos.

### Compreensão de listas

A correta identação é importante!

```python
min_rating = 3.0
filtered_restaurants = [restaurant # retorne todos items
                         for restaurant in restaurants # para cada item na estrutura
                         if restaurant["nota"] > min_rating] # que satisfaça essa condição
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D
```

Podemos filtrar somente uma propriedade do item:
```python
# min_rating = 3.0
filtered_restaurants = [restaurant["name"]  # aqui pedimos somente o nome do restaurante
#                        for restaurant in restaurants
#                        if restaurant["nota"] > min_rating]
# print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D
```
Isto é equivalente às operações de map e filter em JavaScript.

### While

```python
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next
```