names_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def longer(names):
    longer_name = ""
    for name in names:
        if len(name) > len(longer_name):
            longer_name = name
    return longer_name


print(longer(names_list))


# Gabarito
def find_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


# Conclusão: seria melhor definir o valor inicial da variável como o primeiro índice da lista
