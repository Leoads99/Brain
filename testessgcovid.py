import sys
import time
import itertools
from itertools import zip_longest
from colorama import init
init()
from colorama import Fore, init
init()
from colorama import Back, init
init()
import unidecode


print(f'{Back.BLACK} {Fore.WHITE} Copyright (C) Leonardo Andrade de Souza. Todos os direitos reservados.\n')
time.sleep(5)


linha = '-' * 100
print(linha)
titulo = f'{Fore.BLUE} GERENCIADOR COVID-19'
print(titulo.center(100))
print(linha)
time.sleep(5)


#Define uma lista vazia que irá receber os nomes dos pacientes do setor COVID-19
lnome = []
#Define uma lista vazia que irá receber os exames dos pacientes do setor COVID-19
lexames = []


#Define uma função que tira acentuação
def tira_acento_um(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])


#Define uma função que tira acentuação
def tira_acento_dois(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])

        
def removertudo(lista_nomes,lista_exames):
    name_select = str(input(f'{Fore.RED}Qual paciente você gostaria de remover?\n')).upper()
    lista_nomes.remove(name_select)
    exame_select = str(input(f'{Fore.RED}Qual exame desse paciente você irá remover?\n')).upper()
    lista_exames.remove(exame_select)
    
    
#Define uma função que printa as listas 
def mostrar(lista1,lista2):
    print(lista1, lista2)
        
        
acao = 0
while acao != 4:
    print(linha)
    try:
        acao = int(input(Fore.BLUE+'DIGITE\n'
                    f'{Fore.WHITE}[1] para adicionar um paciente e exame realizado\n' 
                    f'{Fore.WHITE}[2] para remover\n' 
                    f'{Fore.WHITE}[3] para exibir os pacientes e exames\n' 
                    f'{Fore.WHITE}[4] para sair\n'))
    except ValueError as err:
        print('OPÇÃO INVÁLIDA!')
    time.sleep(2)
    if acao == 1:
        print('=='*25)
        nome = str(input(f'{Fore.BLUE} Digite o nome do Paciente:\n')).upper()
        print('=='*25)
        lnome.append(nome)
        tira_acento_um(lnome)
        nome = dict(itertools.zip_longest(*[iter(lnome)] * 2, fillvalue=""))
        print(nome)
        time.sleep(2)
        exames = str(input(f'{Fore.BLUE} Digite os exames do Paciente:\n')).upper()
        print('=='*25)
        lexames.append(exames)
        tira_acento_dois(lexames)
        exames = dict(itertools.zip_longest(*[iter(lexames)] * 2, fillvalue=""))
        print(exames)
        time.sleep(2)
        print(lnome)
        print('=='*25)
        print(lexames)
        print('=='*25)
        time.sleep(2)
    if acao == 2:
        input(f'{Fore.BLUE} \nPara remover um paciente, Pressione ENTER para continuar')
        print('=='*25)
        removertudo(lnome,lexames)
        time.sleep(2)
        print(linha)
        print(f'{Fore.BLUE} | PACIENTES | | EXAMES ADICIONADOS| :\n')
        print(linha)
        print(lnome)
        print(lexames)
        time.sleep(2)
    if acao == 3:
        print(linha)
        print(f'{Fore.BLUE} | PACIENTES | | EXAMES ADICIONADOS| :\n')
        print(linha)
        mostrar(lnome,lexames)
        time.sleep(2)
else:
    print (f'{Fore.RED} SAINDO DO GERENCIADOR\n')
    time.sleep(2)
    print(f'{Fore.BLUE} ATÉ LOGO!\n')
    time.sleep(2)
    print(Fore.WHITE+'\nCopyright (C) Todos os direitos reservados, Leonardo Andrade de Souza')
    time.sleep(5)
    sys.exit()