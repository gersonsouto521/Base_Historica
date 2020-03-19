print('empresas cadastradas')
nome_acao = ['ibov', 'itub4', 'itub3', 'itsa4', 'itsa3', 'rail3', 'vale3', 'oibr3', 'oibr4', 'mglu3', 'petr4', 'petr3']
acao_escolhida = []
codigo_empresa = {
        'ibov':'indice-bovespa-IBOV', 
        'itub4':'itauunibanco-pn-ITUB4',
        'itub3':'itauunibanco-on-ITUB3',
        'itsa4':'itausa-pn-ITSA4',
        'itsa3':'itausa-on-ITSA3',
        'rail3':'rumo-on-RAIL3',
        'vale3':'vale-on-VALE3',
        'oibr3':'oi-on-OIBR3',
        'oibr4':'oi-pn-OIBR4',
        'mglu3':'magaz-luiza-on-MGLU3',
        'petr4':'petrobras-pn-PETR4',
        'petr3':'petrobras-on-PETR3',
        }
print('IBOV/ ITUB4/ ITUB3/ ITSA4/ ITSA3/ RAIL3/ VALE3/ OIBR3/ OIBR4/ MGLU3/ PETR4/ PETR3')

def comando():
    codigo_acao = input('Por favor, informe o codigo da Acão: ')
    if codigo_acao.lower() in(nome_acao):
        cod = codigo_empresa[codigo_acao.lower()]
        acao_escolhida.append(cod)
    else:
        print('Desculpe ação invalida, por favor tente novamente: ')
        comando()

comando()
acao_escolhida2 = (acao_escolhida[0])

