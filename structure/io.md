## Input

Sintaxe:
```py
input("Digite uma mensagem:") # retorna sempre str
```

Exemplo:
```python
import random

random_number = random.randint(1, 10)  # escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))  # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)
```

Outra maneira de recebermos valores externos na execução de nossos programas é utilizando o módulo sys . Quando executamos um script e adicionamos parâmetros, os mesmos estarão disponíveis através de uma variável chamada sys.argv , que é preenchida sem que precisemos fazer nada. Na prática, podemos escrever o conteúdo abaixo em um arquivo e, ao executarmos, passamos alguns parâmetros:

```python
import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)
```

Para executarmos passando os parâmetros utilizaremos o comando:
```sh
python3 arquivo.py 2 4 "teste"
```

Saída:
```sh
Received ->  arquivo.py
Received ->  2
Received ->  4
Received ->  teste
```

## Output

### Função print

Sintaxe:
```python
print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42

print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana

print("Em duas ")
print("linhas.")

print("Na mesma", end="")
print("linha.")

# f-string
x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos
```