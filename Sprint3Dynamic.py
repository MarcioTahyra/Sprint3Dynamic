import os
import random
import time

# Função para gerar IDs de exemplo para os usuários

def gerarID(prefix, num):
    return f"{prefix}{num:02d}"

# Função para popular o dicionário com usuários de exemplo, para realizar testes

def popDic(num_alunos, num_profs):
    return {
        'alunos': {
            gerarID("RM", i): {
                "Nome": f"Nome{i}",
                "Histórico": [{'Data': '01/01/24', 'Pontuação': random.randint(1, 100)}]
            } for i in range(1, num_alunos + 1)
        },
        'profs': {
            gerarID("PF", i): {
                "Nome": f"Prof{i}",
                "Turma": random.randint(1, 10)
            } for i in range(1, num_profs + 1)
        }
    }

# Função para popular a lista com usuários de exemplo, para realizar testes

def popList(num_alunos, num_profs):
    return [
        [[gerarID("RM", i), f"Nome{i}", ['01/01/24', random.randint(1, 100)]] for i in range(1, num_alunos + 1)],
        [[gerarID("PF", i), f"Prof{i}", random.randint(1, 10)] for i in range(1, num_profs + 1)]
    ]

# Função para medir o tempo de execução das funções

def medirTempo(func, *args):
    inicio = time.perf_counter()
    func(*args)
    return time.perf_counter() - inicio

# Função de busca por usuário usando Dicionário

def procuraDic(usersDic, id):
    return usersDic['alunos'].get(id) or usersDic['profs'].get(id)

# Função de busca por usuário usando Lista

def procuraList(usersList, id):
    for i in usersList:
        for usuario in i:
            if usuario[0] == id:
                return usuario
    return None

# Função de busca recursiva por usuário usando lista

def procuraRec(lista, id):
    def buscaRec(lista, id):
        for item in lista:
            if isinstance(item, list):
                resultado = buscaRec(item, id)
                if resultado:
                    return resultado
            elif item == id:
                return lista
        return None
    return buscaRec(lista, id)

# Dando 'clear' no console apenas para organização e não confundir os resultados
os.system('cls')

resultados = [[],[],[]]

#  Função que realiza o teste (100 vezes) para todas as abordagens, com o número de usuários escolhido.
#  Então mostra os resultados

def teste(num_alunos, num_profs):
    usersDic = popDic(num_alunos, num_profs)
    usersList = popList(num_alunos, num_profs)

    num_testes = 100
    total_dic = total_list = total_rec = 0

    for _ in range(num_testes):
        id_random = gerarID("RM", random.randint(1, num_alunos)) if random.randint(0, 1) else gerarID("PF", random.randint(1, num_profs))
        total_dic += medirTempo(procuraDic, usersDic, id_random)
        total_list += medirTempo(procuraList, usersList, id_random)
        total_rec += medirTempo(procuraRec, usersList, id_random)

    media_dic = total_dic / num_testes
    media_list = total_list / num_testes
    media_rec = total_rec / num_testes

    print('┌' + '-'*95 + '┐')
    print(f"|\tNúmero de testes: {num_testes} | Quantidade Usuários: {num_alunos + num_profs}" + '\t'*5 + '|')
    print('|' + '-'*95 + '|')
    print(f"|\tMédia de tempo de execução para ProcuraDic: \t{media_dic:.6f} segundos \tO(1)\t\t|")
    print(f"|\tMédia de tempo de execução para ProcuraList: \t{media_list:.6f} segundos \tO(n)\t\t|")
    print(f"|\tMédia de tempo de execução para ProcuraRec: \t{media_rec:.6f} segundos \tO(n) *Recursão\t|")
    print('└' + '-'*95 + '┘\n')
    resultados[0].append(f'{media_dic:.6f}')
    resultados[1].append(f'{media_list:.6f}')
    resultados[2].append(f'{media_rec:.6f}')

# num_alunos = random.randint(10000, 100000)
# num_profs = random.randint(10000, 100000)

# Realização dos teste (100 ~ 10000) usuários

print('\n\t\t\tTestes com 100 a 10000 usuários:')
teste(50,50)
teste(100,100)
teste(250,250)
teste(500,500)
teste(5000,5000)

# Resumo de performance
nome = ['Dicionário:', 'Lista:\t', 'Recursão:']

print('Resumo:\n\nN° de Users:\t 50\t\t| 100\t\t| 500\t\t| 1000\t\t| 10000')
print('-'*91)
for i in range(3):
    print(f'{nome[i]}\t {resultados[i][0]}s\t| {resultados[i][1]}s\t| {resultados[i][2]}s\t| {resultados[i][3]}s\t| {resultados[i][4]}s')
print('\n')