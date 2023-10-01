from docx import Document
import numpy as np

if __name__ == '__main__':
    doc = Document('MT-deterministica.docx')

    # para acessar individualmente uma posição do array, usar array[num][num]
     
    # estados possíveis da MT
    estados = doc.paragraphs[0].text.split(',')

    alfabeto_de_entrada = doc.paragraphs[1].text.split(',')

    alfabeto_da_fita = doc.paragraphs[2].text.split(',')

    #col1               col2        col3            col4        col5 
    #estadoAtual        lendo       proxEstado      escrevo     paraOndeVou

    # todas as transições da MT
    transicoes = [paragrafo.text.replace(";", ",").split(',') for paragrafo in doc.paragraphs[3:22]]

    # especificação dos estados da MT
    estado_inicial = doc.paragraphs[23].text.split(',')
    estado_aceitacao = doc.paragraphs[24].text.split(',')
    estado_rejeicao = doc.paragraphs[25].text.split(',')

    # ------------------------------------------------------------------------------------------------------------------------------------------

    doc2 = Document('entradas.docx') 
    
    # entradas da MT
    entradas = [paragrafo.text for paragrafo in doc2.paragraphs]

    for palavras in entradas:
        for caractere in palavras:
            print(caractere)
            # print(alfabeto_de_entrada, '\n')
            # if caractere in alfabeto_de_entrada:
            #     print('aqui\n') 
        print()