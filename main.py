from docx import Document
import copy
import os

def MT_deterministica():
    doc = Document('MT-deterministica.docx')

    # para acessar individualmente uma posição do array, usar array[num]
     
    # estados possíveis da MT
    estados = doc.paragraphs[0].text.split(',')

    alfabeto_de_entrada = doc.paragraphs[1].text.split(',')

    alfabeto_da_fita = doc.paragraphs[2].text.split(',')

    # para acessar individualmente uma posição do array, usar array[num][num]
    #col1               col2        col3            col4        col5 
    #estadoAtual        lendo       proxEstado      escrevo     paraOndeVou (R ou L)

    # todas as transições da MT
    transicoes = [paragrafo.text.replace(";", ",").split(',') for paragrafo in doc.paragraphs[3:23]]

    # especificação dos estados da MT
    estado_inicial = doc.paragraphs[23].text.split(',')
    estado_aceitacao = doc.paragraphs[24].text.split(',')
    estado_rejeicao = doc.paragraphs[25].text.split(',')

    # ------------------------------------------------------------------------------------------------------------------------------------------

    entrada = input("Digite o nome do arquivo de leitura(incluindo a extensão): ")
    doc2 = Document(entrada)
    
    # entradas da MT
    entradas = [paragrafo.text for paragrafo in doc2.paragraphs]

    for palavras in entradas:
        flag = False
        estado_atual = estado_inicial[0]
        posicao_da_fita = 0
        auxLeitura = 0
        copia = copy.copy(palavras)

        os.system('clear')

        while not flag:
            palavras = list(palavras)
            print("posicao atual da fita: ", posicao_da_fita,"tamanho: ", len(palavras))

            if(auxLeitura == 0 and palavras[posicao_da_fita] not in alfabeto_de_entrada):
                os.system('clear')
                print("Leitura de um caracter inválido!\n")
                break

            if palavras[posicao_da_fita] in alfabeto_da_fita:
                existe_transicao = False

                for t in transicoes:
                    if t[0] == estado_atual and t[1] == palavras[posicao_da_fita] and t[2] in estados and t[3] in alfabeto_da_fita:
                        aux = t
                        existe_transicao = True
                        break
                
                if existe_transicao:
                    palavras[posicao_da_fita] = aux[3]
                    if posicao_da_fita >= 0 and posicao_da_fita <= len(palavras):
                        if aux[4] == 'R':
                            posicao_da_fita += 1
                        elif aux[4] == 'L':
                            auxLeitura = 1
                            posicao_da_fita -= 1 
                        print("estado atual: ", estado_atual," le: ",aux[1]," prox est: ",aux[2]," escrevo: ",aux[3], " acao: ", aux[4])
                        estado_atual = aux[2]
                    else:
                        print("\nFora do intervalo da fita permitido!\n")
                        exit()
                else:
                    os.system('clear')
                    print("Não existe transição do estado ", estado_atual, " lendo ", palavras[posicao_da_fita])
                    print("Posição de parada da cabeça de leitura:", posicao_da_fita)
                    print("Palavra rejeitada pela máquina")
                    break

                if estado_atual in estado_aceitacao:
                    if posicao_da_fita == len(palavras):
                        if palavras[posicao_da_fita - 1] == '_':
                            flag = True
                            os.system('clear')
                            print("A palavra foi aceita pela máquina")
                 
                print("palavra original: ", copia, "\napos alteração: ", ''.join(palavras))
                input("Pressione Enter para continuar...\n")
            else:
                print("Entrada com caracter não pertencente ao alfabeto!")
                break

def MT_nao_deterministica():
    # diferencia-se da MT-deterministica na questão de quando ler um caractere, poder ir para varios estados diferentes
    # modificar o aux para guardar todas as transições possiveis, realizar a tentativa com uma, caso de errado tentar com a outra e assim por diante.
    doc = Document('MT-nao-deterministica.docx')

    # para acessar individualmente uma posição do array, usar array[num]
     
    # estados possíveis da MT
    estados = doc.paragraphs[0].text.split(',')

    alfabeto_de_entrada = doc.paragraphs[1].text.split(',')

    alfabeto_da_fita = doc.paragraphs[2].text.split(',')

    # para acessar individualmente uma posição do array, usar array[num][num]
    #col1               col2        col3            col4        col5 
    #estadoAtual        lendo       proxEstado      escrevo     paraOndeVou (R ou L)

    # todas as transições da MT
    transicoes = [paragrafo.text.replace(";", ",").split(',') for paragrafo in doc.paragraphs[3:30]]

    # especificação dos estados da MT
    estado_inicial = doc.paragraphs[30].text.split(',')
    estado_aceitacao = doc.paragraphs[31].text.split(',')
    estado_rejeicao = doc.paragraphs[32].text.split(',')

    # ------------------------------------------------------------------------------------------------------------------------------------------

    entrada = input("Digite o nome do arquivo de leitura(incluindo a extensão): ")
    doc2 = Document(entrada)
    
    # entradas da MT
    entradas = [paragrafo.text for paragrafo in doc2.paragraphs]

    for palavras in entradas:
        flag = False
        estado_atual = estado_inicial[0]
        posicao_da_fita = 0
        auxLeitura = 0
        copia = copy.copy(palavras)

        os.system('clear')
        
        while not flag:
            palavras = list(palavras)
            print("posicao atual da fita: ", posicao_da_fita,"tamanho: ", len(palavras))
            
            if(auxLeitura == 0 and palavras[posicao_da_fita] not in alfabeto_de_entrada):
                os.system('clear')
                print("Leitura de um caracter inválido!\n")
                break

            if palavras[posicao_da_fita] in alfabeto_da_fita:
                existe_transicao = False
                aux = []

                for t in transicoes:
                    if t[0] == estado_atual and t[1] == palavras[posicao_da_fita] and t[2] in estados and t[3] in alfabeto_da_fita:
                        existe_transicao = True
                        aux.append(t)
                
                print(aux)
                
                openList = [] # estados não visitados
                closedList = [] # estados ja visitados e explorados
                
                if existe_transicao:
                    if len(aux) > 1:
                        pass
                    elif len(aux) == 1:
                        palavras[posicao_da_fita] = aux[0][3]
                        if posicao_da_fita >= 0 and posicao_da_fita <= len(palavras):
                            if aux[0][4] == 'R':
                                posicao_da_fita += 1
                            elif aux[0][4] == 'L':
                                auxLeitura = 1
                                posicao_da_fita -= 1 
                            print("estado atual: ", estado_atual," le: ",aux[0][1]," prox est: ",aux[0][2]," escrevo: ",aux[0][3], " acao: ", aux[0][4])
                            estado_atual = aux[0][2]
                        else:
                            print("\nFora do intervalo da fita permitido!\n")
                            exit()
                else:
                    os.system('clear')
                    print("Não existe transição do estado ", estado_atual, " lendo ", palavras[posicao_da_fita])
                    print("Posição de parada da cabeça de leitura:", posicao_da_fita)
                    print("Palavra rejeitada pela máquina")
                    break

                if estado_atual in estado_aceitacao:
                    if posicao_da_fita == len(palavras):
                        if palavras[posicao_da_fita - 1] == '_':
                            flag = True
                            os.system('clear')
                            print("A palavra foi aceita pela máquina")
                    
                print("palavra original: ", copia, "\napos alteração: ", ''.join(palavras))
                input("Pressione Enter para continuar...\n")
            else:
                print("Entrada com caracter não pertencente ao alfabeto!")
                break

if __name__ == '__main__':
    # usar a função nome-da-string.endswith para diferenciar a extenção do arquivo
    
    # print(entradas)

    # MT_deterministica()
    
    MT_nao_deterministica()
    