import os
task_lst = []
concluida = []
pendente = []
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
        if status == 1:
            stts = 'concluída'
        elif status == 0:
            stts = 'pendente'
        
        tarefa = {
            'descricao': descricao,
            'data': data,
            'status': stts
        }
        task_lst.append(tarefa)
        if status == 1:
            concluida.append(tarefa)
        if status == 0:
            pendente.append(tarefa)
        print("\nTarefa:")
        for chave, valor in tarefa.items():
            print(f'{chave} = {valor}')

        input("\nAperte ENTER para continuar...")
        os.system('cls')
    
    if op == 2:
        os.system('cls')
        for i, t in enumerate(task_lst):
            print('[{0}] Descrição: {1}'.format(i, t['descricao']))
            print('- Data: {1}'.format(i, t['data']))
            print('- Status: {1}'.format(i, t['status']))
            print()
        task = int(input('Digite o valor correspondente a tarefa que deseja editar: '))
        if task > len(task_lst) or task < 0:
            print("Valor inválido!")
        else:
            edit_dc = input("Digite a nova descricao: ")
            edit_dt = input("Digite a nova data: ")
            edit_stt = input("Digite o novo status: ")
            tarefa['descricao'] = edit_dc
            tarefa['data'] = edit_dt
            tarefa['status'] = edit_stt
            task_lst.insert(task,tarefa)
            del task_lst[-1]  
            for i, t in enumerate(task_lst):
                print('[{0}] Descrição: {1}'.format(i, t['descricao']))
                print('- Data: {1}'.format(i, t['data']))
                print('- Status: {1}'.format(i, t['status']))
                print()      
    
    if op == 3:
        for i, t in enumerate(task_lst):
            print('[{0}] Descrição: {1}'.format(i, t['descricao']))
            print('- Data: {1}'.format(i, t['data']))
            print('- Status: {1}'.format(i, t['status']))
            print()
        task = int(input('Digite o valor correspondente tarefa que deseja excluir:'))
        if task > len(task_lst) or task < 0:
            print("Valor inválido!")
        del task_lst[task]
        for i, t in enumerate(task_lst):
            print('[{0}] Descrição: {1}'.format(i, t['descricao']))
            print('- Data: {1}'.format(i, t['data']))
            print('- Status: {1}'.format(i, t['status']))
            print()

        input("\nAperte ENTER para continuar...")
        os.system('cls')

    if op == 4:
        print(f'Total de tarefas: {len(task_lst)}\n')
        print(f'Lista de tarefas:\n')
        print(f'Concluidas: {len(concluida)}\n')
        for i, t in enumerate(concluida):
            print('[{0}] Descrição: {1}'.format(i, t['descricao']))
            print('- Data: {1}'.format(i, t['data']))
            print('- Status: {1}'.format(i, t['status']))
            print()

        print(f'Pendentes: {len(pendente)}\n')
        for i, t in enumerate(pendente):
            print('[{0}] Descrição: {1}'.format(i, t['descricao']))
            print('- Data: {1}'.format(i, t['data']))
            print('- Status: {1}'.format(i, t['status']))
            print()
print("Obrigado por usar o sistema!")
