import xml.etree.ElementTree as ET


# Caminho do arquivo
caminho_arquivo = 'MT-deterministica.txt'

try:
    # Abrir o arquivo para leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Ler o conteúdo do arquivo
        conteudo_xml = arquivo.read()
        print(conteudo_xml)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError:
    print("Ocorreu um erro de I/O ao ler o arquivo.")
# Carregar o conteúdo XML
# conteudo_xml = """
# <?xml version="1.0" encoding="UTF-8" standalone="no"?>
# <structure>
#     ... (conteúdo XML omitido para brevidade)
# </structure>
# """

# Analisar o conteúdo XML
root = ET.fromstring(conteudo_xml)

# Iterar sobre as tags 'state' e 'transition'
for state in root.findall('.//state'):
    state_id = state.get('id')
    state_name = state.get('name')
    print(f'State ID: {state_id}, State Name: {state_name}')

for transition in root.findall('.//transition'):
    from_state = transition.find('from').text
    to_state = transition.find('to').text
    read = transition.find('read').text
    write = transition.find('write').text
    move = transition.find('move').text
    print(f'Transition: From {from_state} to {to_state}, Read: {read}, Write: {write}, Move: {move}')
