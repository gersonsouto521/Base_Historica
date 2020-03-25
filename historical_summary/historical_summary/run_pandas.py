import sqlite3
import pandas as pd


database = sqlite3.connect('../historical_summary/db.sqlite3')
dataset = pd.read_sql_query("SELECT * FROM historical_summary", database)

dataset_5_anos = dataset.loc[dataset['periodo']=='5 Anos'].drop_duplicates(['variacao'])#remove as linhas duplicadas

print('O Relatorio conterá informação da media do periodo de 5 Anos:')
def encerrar_relatorio():
    print('Desculpe informação incorreta')
    encerramento = input('Gostaria de tentar novamente? [1]-SIM // [QQ Tecla] NÃO: ')
    if encerramento == '1':
        relatorio()
    else:
        print('Encerrando o programa!!')

def relatorio():
    print('Relatorio disponiveis [variacao], [vol_med]')
    informe_relatorio = input('Informa o relatorio: ')
    if (informe_relatorio == 'variacao') or (informe_relatorio == 'vol_med'):
        var_bool = input(f'Maior ou Menor {informe_relatorio}: ')
        if (var_bool == 'maior') or (var_bool == 'menor'):
            dic = {'maior':False, 'menor':True}
            print (dic[var_bool])
            ascending_dataset = dataset_5_anos.sort_values(by=informe_relatorio, ascending=dic[var_bool]).head(3)
            print(f'No prazo de 5 Anos segue as empresas com {var_bool}, {informe_relatorio}')
            print (ascending_dataset)
            relatorio()
        else:
            encerrar_relatorio()
    else:
        encerrar_relatorio()
relatorio()




