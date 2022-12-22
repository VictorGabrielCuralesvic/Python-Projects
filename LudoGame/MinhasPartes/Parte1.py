class Infos_do_Jogo:
    def __init__(self):
        self.percurso_normal = 56
        self.percurso_colorido = 6
        self.cores_peoes = ["Azul", "Amarelo", "Vermelho", "Verde"]
        self.numero_de_peoes = 4
        self.dificuldade_bots = 0
        self.hardocore = False


class Jogador:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.ordem_de_jogada = 0
        self.ultima_jogada_do_dado = 0
        self.posicao_no_percurso_normal = 0
        self.percurso_colorico = False
        self.posicao_percurso_colorido = 0
        self.peoes_que_terminaram_o_trageto = 0
        self.peoes_na_zona_neutra = True
        self.bot = False
        self.primeira_jogada = 0

    def __str__(self):
        return f"Jogador: {str(self.nome).title()};Cor da peca: {str(self.cor).title()}"


# Métodos
def Menu1():
    print(f"Menu Principal:\n"
          f"1. Iniciar uma partida\n"
          f"2. Ver as Regras do jogo\n"
          f"3. Tabela dos Campeoes\n"
          f"4. Encerrar o programa\n"
          f"Digite o numero da opcao desejada:")


def Menu_dificildade_dos_bots():
    print(f"Player: voce ira jogar contra bots neste jogo!\nPorvafor escolha uma dificuldade:\n"
          f"1. Facil - Os bot nao tirar numeros altos nos dados.\n"
          f"2. Medio - Os bot tem menos chances de tirar numeros altos no dados.\n"
          f"3. Dificil - Os bots tem as mesmas chances que um Player nos dados\n"
          f"4. Hardcore - O Player tem DESVANTAGEM nos dados em relacao aos bots.\n"
          )


def Regras():
    try:
        a = open("ludo_regras.txt")
    except:
        print("Problemas ao abrir o arquivo de regras")
    else:
        with open("ludo_regras.txt") as arquivo:
            print(arquivo.read() + "\n\n")


def le_quadro_de_campeoes_e_devolve_lista():

    try:
        a = open("quadro_de_campeoes_ludo.txt")
    except:
        print("Problemas ao abrir o arquivo de regras")
    else:
        with open("quadro_de_campeoes_ludo.txt") as arquivo:
            linha_do_arquivo = arquivo.read()
    finally:
        a.close()

    lista_de_10_campeoes = []
    linha_do_arquivo.replace("\n", "")
    lista = linha_do_arquivo.split(";")
    for itens in lista:
        mini_lista_interna = []
        mini_lista_interna = itens.split(",")
        lista_de_10_campeoes.append(mini_lista_interna)
    for elemento in lista_de_10_campeoes:
        elemento[0].replace("\n", "").replace(" ", "")
        elemento[1].replace("\n", "").replace(" ", "")

    return lista_de_10_campeoes


def Mostra_tabela_de_Campeos():
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()

    print("------ Tabela de Campeos ------")
    for campeoes in lista_de_campeos:
        print(f"Campeao: {campeoes[0]} --- Score: {campeoes[1]}")
    print("-------------------------------")


def tem_direito_ao_quadro_dos_campeos(lista_vencedor):
    tem_direito = False
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()

    if (lista_vencedor[4] == True):
        tem_direito = False

    elif (len(lista_de_campeos) < 10):
        tem_direito = True

    elif (len(lista_de_campeos) == 10):
        for campeos_na_lista in lista_de_campeos:
            if (int(lista_vencedor[2]) >= int(campeos_na_lista[1])):
                # nesse if aqui em cima eu comparo os rounds de cada campeao.
                tem_direito = True

    elif (len(lista_de_campeos) > 10):
        print("DEBUG: lista de campeos tem indice maior que 10, arruma isso ai bro heuheueh")

    return tem_direito


def Reorganiza_quadro_de_campeoes(lista_vencedor):
    lista_de_campeos = le_quadro_de_campeoes_e_devolve_lista()
    mini_lista_novo_campeao = []
    mini_lista_novo_campeao.append(lista_vencedor[1])

    mini_lista_novo_campeao.append(str(lista_vencedor[2]))

    if (len(lista_de_campeos) < 10):
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)

    elif (len(lista_de_campeos) == 10):
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)
        lista_de_campeos.pop(10)

    elif (len(lista_de_campeos) > 10):
        print("DEBUG: a lista tem 11 itens, algo aconteceu de errado, vou arrumar agora, nao se preocupe")
        lista_de_campeos.append(mini_lista_novo_campeao)
        lista_de_campeos.sort(key=Funcion_Sort)
        while (len(lista_de_campeos) != 10):
            ultimo_index = int(len(lista_de_campeos)) - 1
            lista_de_campeos.pop(int(ultimo_index))
    lista_aux = []
    for Elementos_lista_com_2_itens in lista_de_campeos:
        string_aux = ""
        string_aux = str(Elementos_lista_com_2_itens[0]) + "," + Elementos_lista_com_2_itens[1]  # nome + , + score
        lista_aux.append(string_aux)

    string_pronta_pra_jogar_no_arquivo = ""
    i = 0
    for elemento in lista_aux:
        if (i == 0):
            string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + str(elemento)
        else:
            string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + ";" + str(elemento)
        i = i + 1
    string_pronta_pra_jogar_no_arquivo = string_pronta_pra_jogar_no_arquivo + "\n"

    try:
        a = open("quadro_de_campeoes_ludo.txt", 'w')
    except:
        print("DEBUG: Erro na hora de abrir o arquivo do quadro de campeos")
    else:
        a.write(string_pronta_pra_jogar_no_arquivo)

    finally:
        a.close()


def Funcion_Sort(item):
    if "\n" in str(item[1]):
        item[1] = str(item[1]).replace("\n", "")
    return str(item[1])


def Funcion_Sort_Ordem_de_Jogada(jogador):
    return int(jogador.primeira_jogada)