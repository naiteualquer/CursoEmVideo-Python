#leia um nome entre quatro alunos

import random

alu1 = input('Digite o nome do aluno 1: ')
alu2 = input('Digite o nome do aluno 2: ')
alu3 = input('Digite o nome do aluno 3: ')
alu4 = input('Digite o nome do aluno 4: ')

listaAlunos = [alu1, alu2, alu3, alu4]
escolheAlunos = random.choice(listaAlunos)

print('O aluno escolhido foi {}' .format(escolheAlunos))

