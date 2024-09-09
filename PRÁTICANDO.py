from prettytable import PrettyTable
informacoesDosUsuarios = []
cont = 1
while True:
    nome = str(input(f"Qual nome da {cont}° pessoa?: "))
    idade = int(input(f"Qual idade de {nome}?: "))
    informacoesDosUsuarios.append({"Nomes": nome, "Idade": idade})
    cont = cont + 1
    while True:
        continuar = input("Você deseja continuar? [S/N]: ").upper().strip()
        if continuar == "S" or continuar == "N":
            break
        print("Opção Inválida!")
    if continuar == "N":
        break
tabela = PrettyTable()
tabela.field_names = informacoesDosUsuarios
print(tabela)
print("Lista de pessoas salvas no programa")
for temp in informacoesDosUsuarios:
    print(f" {temp["Nomes"]}")

