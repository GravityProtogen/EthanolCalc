import random # Para escolher a frase do "você sabia?"
import time # Para animações de calculando.
import os # Os para o clear



def clear():
    """Dá clear na tela do console

    Usa 'cls' no Windows, 'clear' em outros OS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

frases = (
    "Alguns carros possuem uma eficiência energética com etanol maior, enquanto em outros é menor.",
    "O Etanol produz menos gases poluentes quando é queimado.",
    "O Etanol veem de um recurso renovavel: A cana-de-açúcar."
)
frase_escolhida = random.choice(frases)



while True:
    clear()
    z = input("Olá, nos proximos inputs informe o preço do etanol/alcool e o preço da gasolina respectivamente \n \
        Pressione ENTER para continuar(Se deseja desativar animações, digite [N]ão)... ")

    etanol_preco = float(input("Informe o preço do etanol/alcool: "))
    gasolina_preco = float(input("Informe o preço da gasolina: "))


    if z.lower() != "n" and z.lower() != "nao":
        time.sleep(0.5)
        print("Calculando.")
        time.sleep(0.5)
        print("Calculando..")
        time.sleep(0.5)
        print("Calculando...")
        time.sleep(0.5)

    clear()
    x = etanol_preco / gasolina_preco
    if x < 0.7:
        print("Está mais vantajoso utilizar o Alcool")
    else:
        print("Está mais vantajoso utilizar a Gasolina")
    print("Você sabia? ", frase_escolhida)
    x = input("Deseja fazer outro calculo? [S]im ou [N]ão ")
    if x.lower() == 'n' or x.lower() == 'nao':
        clear()
        break
