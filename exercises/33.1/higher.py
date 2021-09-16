# Crie uma função que receba dois números e retorne o maior deles.
def higher(intA, intB):
    if intA > intB:
        return intA
    else:
        return intB


print(higher(10, 20))


# Gabarito
def bigger(number, other):
    if other > number:
        return other
    return number

# Conclusão: else desnecessário
