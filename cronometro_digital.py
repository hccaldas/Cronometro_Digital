# importar biblioteca
import time

#definir função
def cronometro(segundos):
    for s in range(segundos):
        print(f"{segundos - s} segundos restantes.")
        time.sleep(1)
    print("Tempo esgotado!")

#definir segundos
segundos = int(input("Digite a quantidade de segundos: "))
cronometro(segundos)

#definir tempo
tempo = int(input("Digite o tempo em segundos: "))
#contador
cronometro(tempo)