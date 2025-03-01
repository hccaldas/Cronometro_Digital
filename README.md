# Cronômetro Digital em Python

Este repositório contém um script em Python que implementa um cronômetro digital simples. O usuário pode definir a quantidade de segundos e o cronômetro contará regressivamente até zero, exibindo uma mensagem quando o tempo se esgotar.

## Funcionalidades

- Contagem regressiva de segundos.
- Exibição de uma mensagem quando o tempo se esgota.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter o Python 3.x instalado no seu sistema.
3. Execute o script.
4. Insira a quantidade de segundos quando solicitado.
5. O cronômetro começará a contagem regressiva e exibirá uma mensagem quando o tempo se esgotar.

## Exemplo de Uso

```python
# importar biblioteca
import time

# definir função
def cronometro(segundos):
    for s in range(segundos):
        print(f"{segundos - s} segundos restantes.")
        time.sleep(1)
    print("Tempo esgotado!")

# definir segundos
segundos = int(input("Digite a quantidade de segundos: "))
cronometro(segundos)

# definir tempo
tempo = int(input("Digite o tempo em segundos: "))
# contador
cronometro(tempo)
