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


def app(nome_arquivo):
    with open(nome_arquivo,"r",encoding="utf-8") as arquivo:

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
        def CincoPalavras():
            index=0
            menor_palavra="a"
            lista2=[]
            for item1 in lista:
                if len(item1) >= len(menor_palavra):
                    menor_palavra=item1
                    for item2 in range(len(lista)):
                        lista2.append(menor_palavra)
                        break

            novaLista = [palavra1 for palavra1 in reversed(lista2)]
            print(novaLista)
            contador=0;
            for item3 in novaLista:
                print(item3)
                contador=contador+1
                if(contador>=5):
                    break

        #contar Vogais
        def ContarVogais():
            contarA=0
            contarE=0
            contarI=0
            contarO=0
            contarU=0

            for letra in lista:
                
                if "a" in letra or "A" in letra:
                    contarA=contarA+1
                elif "e" in letra or "E" in letra:
                    contarE=contarE+1
                elif "i" in letra or "I" in letra:
                    contarI=contarI+1
                elif "o" in letra or "O" in letra:
                    contarO=contarO+1
                elif "u" in letra or "U" in letra:
                    contarU=contarU+1

            if contarA > contarE and contarA > contarI and contarA > contarO and contarA > contarU:
                print("Existem ",contarA," caracteres A no texto por isso A é a vogal que mais aparece")
            elif contarE > contarA and contarE > contarI and contarE > contarO and contarE > contarU:
                print("Existem ",contarE," caracteres E no texto por isso E é a vogal que mais aparece")
            elif contarI > contarE and contarI > contarA and contarI > contarO and contarI > contarU:
                print("Existem ",contarI," caracteres I no texto por isso I é a vogal que mais aparece")
            elif contarO > contarE and contarO > contarI and contarO > contarA and contarO > contarU:
                print("Existem ",contarO," caracteres O no texto por isso O é a vogal que mais aparece")
            elif contarU > contarE and contarU > contarI and contarU > contarO and contarU > contarA:
                print("Existem ",contarU," caracteres U no texto por isso U é a vogal que mais aparece")
                
        
        #ção
        def VerfificarCao():
            with open("arquivo.txt","r",encoding="utf-8") as arquivo_externo:
                linhas = arquivo_externo.readlines()
            contarLinha = 0
            for linha in linhas:
                if "ção" in linha or "ÇÃO" in linha:
                    print("chegou")
                    contarLinha=contarLinha+1
                    break
                else:
                    contarLinha=contarLinha+1
                    continue
            print("A String Literal ÇÃO esta na linha:",contarLinha)

        CincoPalavras()
        ContarVogais()
        VerfificarCao()

def main():
    return app("arquivo.txt")

main()