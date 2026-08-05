import os
from colorama import Fore, Style, init

init()

ARQUIVO = "alunos.txt"


def titulo(texto):
    print(Fore.BLUE + "\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + Style.RESET_ALL)


def cadastrar():
    titulo("CADASTRAR ALUNO")

    while True:
        nome = input(Fore.LIGHTBLACK_EX + "DIGITE O NOME DO ALUNO(A): \n" + Style.RESET_ALL).strip()

        if nome.strip() == "":
            print(Fore.YELLOW + "NÃO PODE ESPAÇOS VAZIOS\n" + Style.RESET_ALL)
        elif nome.replace(" ", "").isalpha():
            break
        else:
            print(Fore.YELLOW + "DIGITE APENAS LETRAS\n" + Style.RESET_ALL)

    while True:
        try:
            nota = float(input(Fore.LIGHTBLACK_EX + "DIGITE A NOTA DO ALUNO(A): \n" + Style.RESET_ALL).replace(",", "."))

            if 0 <= nota <= 10:
                break
            else:
                print(Fore.YELLOW + "DIGITE APENAS NÚMEROS ENTRE 0 E 10\n" + Style.RESET_ALL)

        except ValueError:
            print(Fore.YELLOW + "DIGITE APENAS NÚMEROS\n" + Style.RESET_ALL)

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome_existente = linha.strip().split(";")[0]

                if nome_existente.lower() == nome.lower():
                    print(Fore.RED + "ALUNO JÁ CADASTRADO, se desejar alterar alguma informação do aluno selecione a opção 3 no menu!\n" + Style.RESET_ALL)
                    return

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{nota}\n")

    print(Fore.GREEN + "Aluno(a) cadastrado com sucesso!\n" + Style.RESET_ALL)


def listar():
    titulo("ALUNOS(A) CADASTRADOS")

    print(Fore.BLUE + "=" * 70 + Style.DIM + Style.RESET_ALL)
    print(f"{'NOME':<35}{'NOTA':>10}{'STATUS':>20}")
    print(Fore.BLUE + "-" * 70 + Style.DIM + Style.RESET_ALL)

    if not os.path.exists(ARQUIVO):
        print(Fore.RED + "Arquivo de cadastro inexistente!\n" + Style.RESET_ALL)
        return

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        alunos = arquivo.readlines()

    if len(alunos) == 0:
        print(Fore.YELLOW + "Nenhum aluno cadastrado.\n" + Style.RESET_ALL)
        return

    for linha in alunos:
        dados = linha.strip().split(";")
        nome = dados[0]
        nota = float(dados[1])

        if nota >= 6:
            situacao = Fore.GREEN + "APROVADO"+ Style.BRIGHT
            nota_cor = Fore.GREEN + f"{nota:.1f}" + Style.RESET_ALL
        else:
            situacao = Fore.RED + "REPROVADO" + Style.RESET_ALL
            nota_cor = Fore.RED + f"{nota:.1f}" + Style.RESET_ALL

        print(f"{nome:<35}{nota_cor:>18}{situacao:>34}")

    print(Fore.BLUE + "=" * 70 + Style.DIM + Style.RESET_ALL)


def alterar():
    titulo("ALTERAR ALUNO(A)")

    if not os.path.exists(ARQUIVO):
        print(Fore.RED + "Arquivo de cadastro inexistente!\n" + Style.RESET_ALL)
        return

    aluno = input(Fore.BLUE + "Digite o nome do aluno(a): \n" + Style.RESET_ALL).strip()

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        alunos = arquivo.readlines()

    encontrado = False
    nova_lista = []

    for linha in alunos:
        nome, nota = linha.strip().split(";")

        if nome.lower() == aluno.lower():
            encontrado = True

            while True:
                novo_nome = input(Fore.LIGHTBLACK_EX + "DIGITE O NOVO NOME DO ALUNO(A):\n" + Style.RESET_ALL)

                if novo_nome.strip() == "":
                    print(Fore.YELLOW + "NÃO PODE ESPAÇOS VAZIOS\n" + Style.RESET_ALL)
                elif novo_nome.replace(" ", "").isalpha():
                    break
                else:
                    print(Fore.YELLOW + "DIGITE APENAS LETRAS\n" + Style.RESET_ALL)

            while True:
                entrada = input(Fore.LIGHTBLACK_EX + "DIGITE A NOVA NOTA DO ALUNO(A):\n" + Style.RESET_ALL).strip()

                if entrada == "":
                    print(Fore.YELLOW + "NÃO PODE ESPAÇOS VAZIOS\n" + Style.RESET_ALL)
                    continue

                try:
                    nova_nota = float(entrada.replace(",", "."))

                    if 0 <= nova_nota <= 10:
                        break
                    else:
                        print(Fore.YELLOW + "APENAS NOTAS ENTRE 0 E 10\n" + Style.RESET_ALL)

                except ValueError:
                    print(Fore.YELLOW + "DIGITE APENAS NÚMEROS\n" + Style.RESET_ALL)

            nova_lista.append(f"{novo_nome};{nova_nota}\n")

        else:
            nova_lista.append(linha)

    if not encontrado:
        print(Fore.RED + "Aluno não encontrado!\n" + Style.RESET_ALL)
        return

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(nova_lista)

    print(Fore.GREEN + "Aluno(a) alterado com sucesso!\n" + Style.RESET_ALL)


def excluir():
    titulo("EXCLUIR ALUNO(A)")

    if not os.path.exists(ARQUIVO):
        print(Fore.RED + "Arquivo de cadastro inexistente!\n" + Style.RESET_ALL)
        return

    aluno = input("Digite o nome do aluno(a): \n").strip()

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        alunos = arquivo.readlines()

    encontrado = False
    nova_lista = []

    for linha in alunos:
        nome, nota = linha.strip().split(";")

        if nome.lower() == aluno.lower():
            encontrado = True
        else:
            nova_lista.append(linha)

    if not encontrado:
        print(Fore.RED + "Aluno(a) não encontrado!\n" + Style.RESET_ALL)
        return

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(nova_lista)

    print(Fore.GREEN + "Aluno(a) excluído com sucesso!\n" + Style.RESET_ALL)


while True:
    titulo("SISTEMA DE CADASTRO DE ALUNOS(A)")

    print(Fore.MAGENTA + "1 - Cadastrar Aluno(a)" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "2 - Listar Aluno(a)" + Style.RESET_ALL)
    print(Fore.CYAN + "3 - Alterar Aluno(a)" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "4 - Excluir Aluno(a)" + Style.RESET_ALL)
    print(Fore.RED + "5 - Sair" + Style.RESET_ALL)

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        alterar()

    elif opcao == "4":
        excluir()

    elif opcao == "5":
        print(Fore.YELLOW + "Programa encerrado.\n" + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "Opção inválida!\n" + Style.RESET_ALL)