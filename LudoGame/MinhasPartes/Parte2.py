'''''''''
if (__name__ == "__main__"):
    infos_do_jogo = Infos_do_Jogo()
    print()
    print("~" * 35)
    print(f"    Bem vindo ao jogo de Ludo!")
    print("~" * 35)
    while (True):
        Menu1()
        resposta_1 = input()
        while resposta_1 not in "1234":
            resposta_1 = input("Entrada invalida, tente novamente:")

        if (int(resposta_1) == 1):
            # inicia um novo jogo
            print("\n---Novo Jogo---")

            numero_de_jogadores = input("Quantos players humanos iram jogar?")  # melhorar essa pergunta ai que ta feio
            while (numero_de_jogadores not in "1234"):
                numero_de_jogadores = input("Porfavor digite um numero inteiro de 1 a 4:")
            if(int(numero_de_jogadores) < 4):
                Menu_dificildade_dos_bots()
                resposta_menu_dificuldade_bots = input("Digite a opcao escolhida: ")
                while resposta_menu_dificuldade_bots not in "1234":
                    resposta_menu_dificuldade_bots = input("Digite uma opcao valida(1 a 4): ")
                if(resposta_menu_dificuldade_bots == 4):
                    infos_do_jogo.hardocore = True
                    infos_do_jogo.dificuldade_bots = 3
                else:
                    infos_do_jogo.dificuldade_bots = resposta_menu_dificuldade_bots
            print("\n")

            lista_de_jogadores = Cria_Objeto_Jogador(numero_de_jogadores)

            Partida_do_jogo(lista_de_jogadores)


        elif (int(resposta_1) == 2):
            Regras()

        elif (int(resposta_1) == 3):
            Mostra_tabela_de_Campeos()

        elif (int(resposta_1) == 4):
            Sair = input("Voce deseja realmente sair?(S/N)")
            while Sair.upper() not in "SN":
                Sair = input("entrada invalida, tente novamente(S/N):")
            if (Sair.upper() == "S"):
                print("Encerrando o programa...")
                break
            else:
                pass
'''''''''''