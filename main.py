from docx import Document
import copy

if __name__ == '__main__':
    doc = Document('MT-deterministica.docx')

    # para acessar individualmente uma posição do array, usar array[num]
     
    # estados possíveis da MT
    estados = doc.paragraphs[0].text.split(',')
    # print(estados)

    alfabeto_de_entrada = doc.paragraphs[1].text.split(',')

    alfabeto_da_fita = doc.paragraphs[2].text.split(',')

    # para acessar individualmente uma posição do array, usar array[num][num]
    #col1               col2        col3            col4        col5 
    #estadoAtual        lendo       proxEstado      escrevo     paraOndeVou (R ou L)

    # todas as transições da MT
    transicoes = [paragrafo.text.replace(";", ",").split(',') for paragrafo in doc.paragraphs[3:22]]
    # print(transicoes)

    # especificação dos estados da MT
    estado_inicial = doc.paragraphs[23].text.split(',')
    estado_aceitacao = doc.paragraphs[24].text.split(',')
    estado_rejeicao = doc.paragraphs[25].text.split(',')

    # ------------------------------------------------------------------------------------------------------------------------------------------

    doc2 = Document('entradas.docx') 
    
    # entradas da MT
    entradas = [paragrafo.text for paragrafo in doc2.paragraphs]
    estado_atual = estado_inicial[0]
    

    # print(entradas)

    for palavras in entradas:
        flag = False
        posicao_da_fita = 0
        copia = copy.copy(palavras)

        # print(caractere)
        # print(alfabeto_de_entrada, '\n')
        print('tamanho: ', len(palavras))
        while not flag:
            print('posicao atual da fita: ', posicao_da_fita)
            if palavras[posicao_da_fita] in alfabeto_da_fita:
                
                # para cada caracter da entrada
                # verificar em qual estado estamos
                      
                for t in transicoes:
                    if estado_atual in estado_rejeicao:
                        # se o estado atual existe
                        # e o caracter atual da entrada é igual caracter da transicao atual
                        if t[0] == estado_atual and palavras[posicao_da_fita] == t[1]:
                            # se for igual, precisamos ver para qual estado a transicao direciona
                            if t[2] in estados and t[3] in alfabeto_da_fita:
                                palavras = palavras.replace(palavras[posicao_da_fita], t[3], 1)
                                print('acao: ', t[4])
                                if posicao_da_fita >= 0 and posicao_da_fita <= len(palavras):
                                    if t[4] == 'R':
                                        posicao_da_fita += 1
                                    elif t[4] == 'L':
                                        posicao_da_fita -= 1 
                                    estado_atual = t[2]
                                    print('estado atual: ', estado_atual)
                                    break
                    elif estado_atual in estado_aceitacao and palavras[posicao_da_fita] == '_':
                        flag = True
                        break
                print('palavra original: ', copia)
                print('apos alteracao: ', palavras)
                input("Pressione Enter para continuar...")
            else:
                print("Entrada com caracter não pertencente ao alfabeto!")
                break