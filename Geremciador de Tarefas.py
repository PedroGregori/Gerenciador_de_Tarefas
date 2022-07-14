""" Gerenciador de tarefas
    1 - Adicionar
    2 - Editar
    3 - Excluir
    4 - Listar tarefas concluídas
    5 - Listar tarefas pendentes
"""
import os
task_lst = []
op = 0
while op != 5:
    print('[1] Adicionar\n[2] Editar\n[3] Excluir\n[4] Gerar relatório das tarefas\n[5] Sair')
    op = int(input("O que deseja fazer?: "))
    if op == 1:
        os.system('cls')
        print("## Cadastro de tarefa ##\n")
        descricao = input("Descrição da tarefa: ")
        data = input("Data: ")
        status = int(input("Status [0] pendente, [1] concluída: "))

        tarefa = {
            'descricao': descricao,
            'data': data,
            'status': status
        }
        task_lst.append(tarefa)

        print("\nTarefa:")
        for chave, valor in tarefa.items():
            print(f'{chave} = {valor}')

        input("\nAperte ENTER para continuar...")
        os.system('cls')
    
    if op == 2:
        task = int(input('Digite o valor correspondente a tarefa que deseja editar:'))
        for i, t in enumerate(task_lst):
            print('[{0}] - {1}'.format(i, t['descricao']))
        edit = input("Digite a nova tarefa: ")
        tarefa[task] = edit 
    
    if op == 3:
        task = int(input('Digite o valor correspondente tarefa que deseja excluir:'))
        for i, t in enumerate(task_lst):
            print('[{0}] - {1}'.format(i, t['descricao']))


        # pegar a o valor digitado pelo usuário 
        # e comparar com o tamanho da lista.
        # Se for maior do que a lista é um valor inválido.

    if op == 4:
        os.system('cls')
        print('Total de tarefas: ', len(task_lst))
        print('Lista de tarefas:')
        for t in task_lst:
            print(t)
print("Obrigado por usar o sistema!")
os.system('cls')