# Modulo de controle de autenticação
# author: Emerson J.S.Costa
# ctt: junior.emerson5@aluno.ufsj.edu.br
# O arquivo recebido tem que ser um json com um cabeçalho especificando o processo que deve ser processado
#ex.:
#[{ process: Login data:...}]

def principal(ws):
    while True:
        data = ws.receive()