import math
COVERAGE_BY_LITER = 3
CAN_VOLUME = 18
PRICE_PER_CAN = 80


def paint(meters):
    liters = meters / COVERAGE_BY_LITER
    cans = math.ceil(liters / CAN_VOLUME)
    total_price = cans * PRICE_PER_CAN
    return (cans, total_price)


print(paint(80))


# Gabarito
def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price

# Conclusão: não necessário definir constantes; cálculo de latas sem precisar usar o método ceil
