# arquiva até 5 nomes

lista = ['Ana' , 'José']

'''Define "adicionar" como uma cadeia de comandos para colocar a variavel na lista'''

def checar():
    return len(lista)
    
def adicionar(n):
    lista.append(n)
    
while len(lista) <= 4:
    print("hão" , len(lista) , "nomes salvos")
    nome = input("Insira um nome: \n")
    adicionar(nome)
    print("Nome adicionado com sucesso")
    print("os nomes na lista são:" , lista)
    sn = input("Adicionar mais um nome? S/N \n")
    if sn == "n":
        print(len(lista) , "Nomes adicionados com sucesso")
        break
    elif sn == "s":
        continue
    else:
        print("comando inválido, tente novamente")
        
    if len(lista) == 5:
        print("A quantidade máxima de nomes já foi atingida")
        y = input("Deseja apagar os nomes na lista e recomeçar? \n")
    if y == "s":
        lista.clear()
        print("Agora tem", len(lista) , "nomes na lista")
    else:
        print("Obrigado por usar o armazenador de nomes")