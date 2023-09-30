from docx import Document
import numpy as np

if __name__ == '__main__':
    doc = Document('MT-deterministica.docx')

    # LER A LINHA, SEPARAR PELA VIRGULA E ADICIONAR OS ITENS SEPARADOS

    # para acessar individualmente uma posição do array, usar array[num][num]
     
    # estados possíveis da MT
    estados = np.array([doc.paragraphs[0].text.replace("'", "").replace(";", "")])

    alfabeto_de_entrada = np.array([doc.paragraphs[1].text])

    alfabeto_da_fita = np.array([doc.paragraphs[2].text.replace(",", "").replace(";", "")])

    #col1               col2        col3            col4        col5 
    #estadoAtual        lendo       proxEstado      escrevo     paraOndeVou

    # todas as transições da MT
    transicoes = np.array([paragrafo.text.replace(",", "").replace(";", "") for paragrafo in doc.paragraphs[3:22]])

    # especificação dos estados da MT
    estado_inicial = np.array([doc.paragraphs[23].text.replace(",", "").replace(";", "")])
    estado_aceitacao = np.array([doc.paragraphs[24].text.replace(",", "").replace(";", "")])
    estado_rejeicao = np.array([doc.paragraphs[25].text.replace(",", "").replace(";", "")])

    # ------------------------------------------------------------------------------------------------------------------------------------------

    doc2 = Document('entradas.docx') 
    
    # entradas da MT
    entradas = np.array([paragrafo.text for paragrafo in doc2.paragraphs])

    for palavras in entradas:
        for caractere in palavras:
            # print(caractere, '\n')
            print(alfabeto_de_entrada, '\n')
            if caractere in alfabeto_de_entrada:
                print('aqui\n') 