# Inicialização de variáveis
alunos = []
disciplinas = ["Algoritmos", "Segurança", "Desenv. Web"]

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    if len(alunos) < 15:
        matricula = int(input("Digite a matrícula do aluno: "))
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        aluno = {"matricula": matricula, "nome": nome, "idade": idade, "notas": [[0]*5 for _ in range(3)]}
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    else:
        print("Limite de alunos cadastrados atingido!")

# Função para incluir notas
def incluir_notas():
    matricula = int(input("Digite a matrícula do aluno: "))
    disciplina = int(input("Digite o código da disciplina (0 - Algoritmos, 1 - Segurança, 2 - Desenv. Web): "))
    if disciplina >= 0 and disciplina < 3:
        notas = []
        for i in range(5):
            nota = float(input(f"Digite a {i+1}ª nota (0 a 10): "))
            while nota < 0 or nota > 10:
                nota = float(input("Nota inválida. Digite uma nota entre 0 e 10: "))
            notas.append(nota)
        for aluno in alunos:
            if aluno["matricula"] == matricula:
                aluno["notas"][disciplina] = notas
                print("Notas incluídas com sucesso!")
                return
        print("Matrícula não encontrada.")
    else:
        print("Código de disciplina inválido.")

# Função para calcular a média de notas de um aluno
def calcular_media(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            notas = aluno["notas"]
            media = sum(sum(nota) for nota in notas) / 15
            return media
    return None

# Função para exibir informações de um aluno
def consultar_informacoes_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Nome: {aluno['nome']}")
            for i, disciplina in enumerate(disciplinas):
                notas = aluno["notas"][i]
                media = sum(notas) / 5
                print(f"{disciplina}: {notas} (Média: {media})")
            return
    print("Matrícula não encontrada.")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar um novo aluno")
    print("2. Incluir notas")
    print("3. Consultar informações de um aluno")
    print("4. Gerar relatório de desempenho")
    print("5. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        incluir_notas()
    elif opcao == 3:
        consultar_informacoes_aluno()
    elif opcao == 4:
        matricula = int(input("Digite a matrícula do aluno para gerar o relatório de desempenho: "))
        media = calcular_media(matricula)
        if media is not None:
            print(f"Média de notas do aluno: {media}")
        else:
            print("Matrícula não encontrada.")
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")