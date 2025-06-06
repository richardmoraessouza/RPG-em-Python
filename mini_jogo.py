from modulos_jogo import traços, limpar_tela, nome_jogador, começando_jg
from time import sleep

bem_vindo = "Bem vindo!, A meu jogo"
traços()
print(f"{bem_vindo:>40}")
traços()
jogar = input("Vai querer \033[32mjogar\033[m?\n").strip().lower()
while True:
    if jogar == "sim" or jogar == "s":
        print("\033[32mIniciando o jogo...\033[m")
        nome_jogador()
        break
    elif jogar == "não" or jogar == "n":
        limpar_tela()
        print("\033[34msaindo do jogo...\033[m")
        sleep(2)
        break
    else:
        while True:
         print("Digite sim ou não!")
         jogar = input("").lower().strip()
         if jogar == "sim" or jogar == "s":
            break
         elif jogar == "não" or jogar == "n":
            break
         