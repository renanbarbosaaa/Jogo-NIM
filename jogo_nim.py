def computador_escolhe_jogada(n, m):
    r = n % (m + 1)
    if r == 0:
        return m if n >= m else n
    return r

def usuario_escolhe_jogada(n, m):
    while True:
        try:
            x = int(input("Quantas peças você vai tirar? "))
        except ValueError:
            print("Oops! Jogada inválida! Tente de novo.")
            continue

        if 1 <= x <= m and x <= n:
            return x
        else:
            print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    computador_joga = (n % (m + 1) != 0)
    if computador_joga:
        print("\nComputador começa!\n")
    else:
        print("\nVoce começa!\n")

    restantes = n
    vez_computador = computador_joga

    while restantes > 0:
        if vez_computador:
            tirada = computador_escolhe_jogada(restantes, m)
            restantes -= tirada
            if tirada == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {tirada} peças.")
        else:
            tirada = usuario_escolhe_jogada(restantes, m)
            restantes -= tirada
            if tirada == 1:
                print("Voce tirou uma peça.")
            else:
                print(f"Voce tirou {tirada} peças.")

        if restantes > 1:
            print(f"Agora restam {restantes} peças no tabuleiro.\n")
        elif restantes == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")

        vez_computador = not vez_computador

    print("Fim do jogo! O computador ganhou!\n")
    return "computador"

def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****\n")
        vencedor = partida()
        if vencedor == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1

    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato", end=" ")

    while True:
        try:
            escolha = int(input())
            if escolha in (1, 2):
                break
        except ValueError:
            pass
        print("Opção inválida! Tente de novo.")

    if escolha == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    else:
        campeonato()

if __name__ == "__main__":
    main()
