import random
import time
import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

frases = \
    ("Alguns carros possuem uma eficiência energética com etanol maior, enquanto em outros é menor.", \
    "O Etanol produz menos gases poluentes quando é queimado.", \
    "O Etanol veem de um recurso renovavel: A cana-de-açúcar.")
frase_escolhida = random.choice(frases)



while True:
    Clear()
    input("Olá, nos proximos inputs informe o preço do etanol/alcool e o preço da gasolina respectivamente \n \
        Pressione ENTER para continuar...")

    etanol_preço = float(input("Informe o preço do etanol/alcool: "))
    gasolina_preço = float(input("Informe o preço da gasolina: "))

    time.sleep(0.3)
    print("Calculando.")
    time.sleep(0.3)
    print("Calculando..")
    time.sleep(0.3)
    print("Calculando...")
    time.sleep(0.3)

    Clear()
    x = etanol_preço / gasolina_preço
    if(x < 0.7):
        print("Está mais vantajoso utilizar o Alcool")
    else:
        print("Está mais vantajoso utilizar a Gasolina")
    print("Você sabia? ", frase_escolhida)
    x = input("Deseja fazer outro calculo? [S]im ou [N]ão ")
    if x.lower() == 'n' or x.lower() == 'nao':
        Clear()
        break