from random import choice, randint
# richard!, a vida dos monstros que vc mata não recupera, eles ficam mortos até o fim do programa.
# arrume zé cu
from time import sleep
abate = 0
hit_kill = 0
pontos = 0
lista_de_pontos = {"zumbi": 50,
                   "slime": 100,
                   "goblin": 25,
                   "titã": 150,
                   "soberano": 200
}

def recuperar_vida():
    será = ["sim", "não", "não", "sim", "não", "não,", "não", "não", "não", "não", "não", "não", "não"]
    sim_não = choice(será)
    if sim_não == "sim":
        global poção_escolhida, vida
        recuperação_de_vida = {
                            "vida nivel 1": 5,
                            "vida nivel 2": 10,
                            "vida nivel 3": 15,
                            "vida nivel 4": 20,
                            "vida nivel 5": 25,
                            "vida nivel 6": 30,
                            "vida nivel 7": 35,
                            "vida nivel 8": 40,
                            "vida nivel 9": 45,
                            "vida nivel 10": 50
                            }
        escolhendo_poção = choice(list(recuperação_de_vida))
        poção_escolhida = recuperação_de_vida[escolhendo_poção]
        print(f"vc recuperou \033[32m{poção_escolhida}\033[m de vida".center(30, " "))
        vida += poção_escolhida
    else:
        None

def estatísticas_finais():
    global abate
    global hit_kill
    print(f"Jogador: {nome}")
    print(f"matou {abate} monstros")
    print(f"Hit kills: {hit_kill}")
    print(f"Pontuação final: {pontos}")
    ranke = None
    if pontos == 0:
        print("Vc fez \033[31mzero pontos\033[m")
    elif pontos >= 0 and pontos <= 100 :
        ranke = "Broze"
    elif pontos >=100 and pontos <= 250:
        ranke = "Prata"
    elif pontos >= 250 and pontos <= 378:
        ranke = "Ouro"
    elif pontos >= 378 and pontos <= 500:
        ranke = "Platina"
    elif pontos >= 500 and pontos <= 600:
        ranke = "Esmeralda"
    elif pontos >= 600 and pontos <= 700:
        ranke = "Diamante"
    elif pontos >=700 and pontos <= 800:
        ranke = "Mestre"
    elif pontos >= 800 and pontos <= 900:
        ranke = "Grão-Mestre"
    elif pontos >= 1000:
        ranke = "Desafiante"
    print(f"Seu elo: {ranke}")
    return

def limpar_tela():
    # Só para limpar a tela mesmo
    import os
    os.system('cls' if os.name == "nt" else "clear")

def mobs():
    # Aqui onde escolhe a mob que vai lutar com o jogador
    global dados_dos_mobs
    global escolhendo_mob
    dados_dos_mobs = {
       "zumbi": {"vida": 10, "dano": randint(1, 10), "nivel": 5},
       "slime": {"vida": 20, "dano": randint(1, 15), "nivel": 10},
       "titã": {"vida": 40, "dano": randint(10, 25), "nivel": 20},
       "soberano": {"vida": 30, "dano": randint(5, 20),"nivel": 15},
       "goblin": {"vida": 7, "dano": randint(1, 7), "nivel": 1},
       }
    
    escolhendo_mob = choice(list(dados_dos_mobs.keys()))
    começando_jg(escolhendo_mob)
    
def nome_jogador():
    # Onde o jogador coloca o nome dele
    global nome, vida
    vida = 100
    nome = input("Digite seu nome: ")
    print("-"*10)
    print("/", f"\033[32m{nome:>5}\033[m", "/")
    print("-"*10)
    limpar_tela()
    mobs()

def hora_da_luta(mob, dados_dos_mobs):
    cont = 0
    # Aqui onde começa a batalha
    global abate, pulos, hit_kill, pontos, vida
    if dados_dos_mobs[mob]['vida'] < 1:
         return
    
    if vida < 1:
         return
    
    detalhes = f"Estatísticas sobre o {mob}"
    print(f"{detalhes:>40}")
    traços()
    print(f"Nivel {dados_dos_mobs[mob]['nivel']}")
    print(f"Vida: {dados_dos_mobs[mob]['vida']}")
    print(f"Dano: {dados_dos_mobs[mob]['dano']}")
    print("-="*10)
    ver_estatística = input("")

    while True:
        print(f"{mob:>30}")
        traços()
        dano_do_jogador = randint(1, 30)
        dados_dos_mobs[mob]["vida"] -= dano_do_jogador
        vida -= dados_dos_mobs[mob]['dano']
        print(f"\033[34m{nome}\033[m!, Deu \033[32m{dano_do_jogador}\033[m de dano no \033[31m{mob}\033[m")
        print(f"\033[31m{mob}!, deu \33[31m{dados_dos_mobs[mob]['dano']}\033[m de dano no \033[34m{nome}\033[m")
        print(f"\033[32mVida\033[m: \033[42m{vida}\033[m")
        print(f"\033[31m{mob}\033[m: \033[31m{dados_dos_mobs[mob]['vida']}\033[m")
        recuperar_vida()
        cont += 1
        if dados_dos_mobs[mob]['vida'] <=0:
            if cont == 1:
              print("\033[4;31mHIT KILL\033[m".center(40, " "))
              hit_kill += 1

            if lista_de_pontos[mob]:
                pontos += lista_de_pontos[mob]

            abate += 1
            traços()
            print(f"O \033[31m{mob}\033[m morreu".center(50, " "))
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f"vida do {mob}:", "\033[41m/", " "*5, "0", " "*5, "/\033[m")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            dados_dos_mobs[mob]['vida'] += dados_dos_mobs[mob]['vida']
            print("procurando outro \033[31mmonstro\033[m...")
            sleep(3)
            limpar_tela()
            break

        if vida < 1:
            break

        continuar = input("Vai querer lutar ainda?\n")
        limpar_tela()
        if continuar == "não" or continuar == "n":
            if pulos >= 1:
                pulos -= 1
                print("-"*6)
                print("/", f"\033[32m{pulos:<2}\033[m", "/")
                print("-"*6)
                break
            else:
                 aviso = "\033[33mAVISO\033[m"
                 print(f"{aviso:>30}")
                 traços()
                 print("\033[31mVocê não pode pular mais!\033[m")
                 print(f"Por conta de seus pulo estárem em {pulos}")
                 enter = input("")
                 limpar_tela()
                 continue
                 
        elif continuar == "sim" or continuar == "s":
            None

        else:
            while True:
                print("Digite sim ou não")
                continuar = input("Vai querer lutar ainda?\n").strip().lower()
                if continuar == "n" or continuar == "não":
                    break
                elif continuar == "s" or continuar == "não":
                    break
                print("erro 1")

        if continuar == "n" or continuar == "não":
            pulos -= 1
            print("-"*6)
            print("/", f"\033[32m{pulos:<2}\033[m", "/")
            print("-"*6)
            break

def traços():
    # para colocar os traços mais rapido
    print("-="*30)

def começando_jg(mob_escolhido):
    from random import choice, randint
    from time import sleep
    # Aqui é a decisão do jogador, se ele vai querer não lutar com mob ou vai desistir de lutar
    global vida , pulos
    pulos = 10
    while True:
        if vida < 1:
            #    quando o jogador morre
               traços()
               morte_player = "\033[31mVocê Morreu!\033[m"
               print(f"{morte_player:>45}")
               traços()

               while True:
                continuar = str(input(f"\033[34m{nome}\033[m!, Vai querer continuar jogando!")).strip().lower()
                if continuar == "sim" or continuar == "s":
                    vida += 100
                    recomeçando = "\033[32mcomeçando\033[m"
                    print(f"{recomeçando:>40}")
                    break

                elif continuar == "n" or continuar == "não":
                    print("\033[34mSaindo do jogo...\033[m")
                    estatísticas_finais()
                    return

        mob_escolhido = choice(list(dados_dos_mobs.keys()))
        print(f"Apareceu um {mob_escolhido}, \033[32m{nome}\033[m vai querer com o monstro?")
        print("Digite não para pular o monstro!.\nDigite parar ou desistir para sair da luta.")
        traços()
        decisão = input("").strip().lower()
        limpar_tela()

        if decisão == "sim" or decisão == "s":
                hora_da_luta(mob_escolhido, dados_dos_mobs)

        elif decisão == "sair":
                print("\033[34mSaindo do jogo...\033[m")
                estatísticas_finais()
                return
        
        elif decisão == "não" or decisão == "n":
                if pulos >= 1:
                    pulos -= 1
                    print("-"*6)
                    print("/", f"\033[32m{pulos:>2}\033[m", "/")
                    print("-"*6)

                else:
                    aviso = "\033[33mAVISO\033[m"
                    print(f"{aviso:>30}")
                    traços()
                    print("\033[31mVocê não pode pular mais!\033[m")
                    print(f"Por conta de seus pulo estárem em {pulos}")
                    enter = input("")
                    hora_da_luta(mob_escolhido, dados_dos_mobs) 

        else:
            digite = "\033[33mDIGITE\033[m"

            while True:
                print(F"{digite:>30}")
                traços()
                print(".\033[33msim\033[m para lutar")
                print(".\033[33mnão\033[m para pular a batalha")
                print(".\033[33msair\033[m para sair do jogo")
                decisão = input("").strip().lower()

                if decisão == "sim" or decisão == "s":
                     hora_da_luta(mob_escolhido, dados_dos_mobs)
                     break
                elif decisão == "sair":
                     print("\033[34mSaindo do jogo...\033[m")
                     estatísticas_finais()
                     break
                
                elif decisão == "não" or decisão == "n":
                     if pulos >= 1:
                        pulos -= 1
                        print("-"*6)
                        print("/", f"\033[32m{pulos:>2}\033[m", "/")
                        print("-"*6)
                        break
                     
                     else:
                          aviso = "\033[33mAVISO\033[m"
                          print(f"{aviso:>30}")
                          traços()
                          print("\033[31mVocê não pode pular mais!\033[m")
                          print(f"Por conta de seus pulo estárem em {pulos}")
                          enter = input("")
                          hora_da_luta(mob_escolhido, dados_dos_mobs)
        if decisão == "sair":
             break