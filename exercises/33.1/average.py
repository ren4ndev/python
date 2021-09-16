from statistics import mean


# Calcule a média aritmética dos valores contidos em uma lista.
def average(*numbers):
    avg = 0
    for number in numbers:
        avg += number
    return avg / len(numbers)


print(average(5, 10, 15))

# Utilizando o método mean do módulo statistcs
print(mean([5, 10, 15]))


# Gabarito
def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


# Conclusão: great!
