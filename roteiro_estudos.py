import datetime

def capturar_horario_atual():
    return datetime.datetime.now()

def calcular_tempo_estudado(inicio, fim):
    return fim - inicio

def salvar_roteiro_txt(roteiro):
    materias = set(entrada['Matéria/Assunto'] for entrada in roteiro)
    for materia in materias:
        nome_arquivo = f"{materia}.txt"
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for i, entrada in enumerate(roteiro, 1):
                if entrada['Matéria/Assunto'] == materia:
                    arquivo.write(f"--- Entrada {i} ---\n")
                    arquivo.write(f"Data Início: {entrada['Data Início'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                    arquivo.write(f"Data Fim: {entrada['Data Fim'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                    arquivo.write(f"Tempo Estudado: {entrada['Tempo Estudado']}\n")
                    arquivo.write(f"Matéria/Assunto: {entrada['Matéria/Assunto']}\n")
                    arquivo.write(f"Anotações: {entrada['Anotações']}\n")
                    arquivo.write("-------------------\n\n")
        print(f"Roteiro salvo em {nome_arquivo}")

def adicionar_entrada(roteiro):
    input("Pressione Enter para marcar o início do estudo...")
    data_inicio = capturar_horario_atual()
    print(f"Estudo iniciado em: {data_inicio.strftime('%Y-%m-%d %H:%M:%S')}")
    
    materia = input("Digite a matéria ou assunto: ")
    anotacoes = input("Digite suas anotações, dúvidas ou comentários: ")
    
    input("Pressione Enter para marcar o término do estudo...")
    data_fim = capturar_horario_atual()
    print(f"Estudo terminado em: {data_fim.strftime('%Y-%m-%d %H:%M:%S')}")
    
    tempo_estudado = calcular_tempo_estudado(data_inicio, data_fim)
    
    entrada = {
        'Data Início': data_inicio,
        'Data Fim': data_fim,
        'Tempo Estudado': tempo_estudado,
        'Matéria/Assunto': materia,
        'Anotações': anotacoes
    }
    
    roteiro.append(entrada)
    print("Entrada adicionada com sucesso!")

def mostrar_roteiro(roteiro):
    if not roteiro:
        print("Nenhuma entrada no roteiro.")
        return
    
    for i, entrada in enumerate(roteiro, 1):
        print(f"--- Entrada {i} ---")
        print(f"Data Início: {entrada['Data Início'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Data Fim: {entrada['Data Fim'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Tempo Estudado: {entrada['Tempo Estudado']}")
        print(f"Matéria/Assunto: {entrada['Matéria/Assunto']}")
        print(f"Anotações: {entrada['Anotações']}")
        print("-------------------\n")

def main():
    roteiro = []
    
    while True:
        print("1. Adicionar entrada ao roteiro")
        print("2. Mostrar roteiro")
        print("3. Salvar roteiro em arquivo txt e sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_entrada(roteiro)
        elif opcao == '2':
            mostrar_roteiro(roteiro)
        elif opcao == '3':
            salvar_roteiro_txt(roteiro)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
