#Crie um programa que recebe como argumento um arquivo texto(path), o programa deve #ler o arquivo e imprimir

#1-quantas palavras existem no arquivo
#2-as 5 maiores palavras(quant carácter)
#3-qual a vogal que mais parece
#4-caso tenha o literal “ção” informar que linha do texto ocorre essa primeira aparição


#regras
#1-escolha a linguagem
#2-faça pelo menos um subprograma para cada objetivo
#3-use parâmetros ao menos em um programa
#4-use return literal

#Abrir e Ler o Arquivo
arquivo = open("arquivo.txt","r",encoding="utf-8")

#Organizo uma Lista
contador=0
tira_chars = arquivo.read()
caracteres = ",:.;!?"
for i in range(len(caracteres)):
    tira_chars=tira_chars.replace(caracteres[i],"")

lista = tira_chars.split(" ")

for item in lista:
    contador=contador+1
       
print(lista)  
print("quantidade de palavras ",contador);
print("\n")

#vejo as maiores 5 palavras
index=0
menor_palavra="a"
lista2=[]
for item1 in lista:
    if len(item1) >= len(menor_palavra):
        menor_palavra=item1
        for item2 in range(len(lista)):
            lista2.append(menor_palavra)
            break

novaLista = [num for num in reversed(lista2)]
print(novaLista)
contador=0;
for item3 in novaLista:
    print(item3)
    contador=contador+1
    if(contador>=5):
        break

#contar Vogais

#contarA=0
#contarE=0
#contarI=0
#contarO=0
#contarU=0

#for vogal in lista:
#    if

#ção
    
            
            
        
    



arquivo.close()