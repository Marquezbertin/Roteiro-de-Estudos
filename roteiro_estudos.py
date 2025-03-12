import datetime
import tkinter as tk
from tkinter import messagebox

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

def adicionar_entrada(roteiro, materia, anotacoes, data_inicio, data_fim):
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

def iniciar_interface():
    roteiro = []
    data_inicio = None

    def iniciar_estudo():
        nonlocal data_inicio
        data_inicio = capturar_horario_atual()
        lbl_status.config(text=f"Estudo iniciado em: {data_inicio.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def pausar_estudo():
        nonlocal data_inicio
        if data_inicio:
            data_fim = capturar_horario_atual()
            materia = entry_materia.get()
            anotacoes = entry_anotacoes.get("1.0", tk.END).strip()
            adicionar_entrada(roteiro, materia, anotacoes, data_inicio, data_fim)
            lbl_status.config(text=f"Estudo pausado em: {data_fim.strftime('%Y-%m-%d %H:%M:%S')}")
            data_inicio = None
        else:
            messagebox.showwarning("Aviso", "O estudo não foi iniciado.")
    
    def encerrar_estudo():
        nonlocal data_inicio
        if data_inicio:
            data_fim = capturar_horario_atual()
            materia = entry_materia.get()
            anotacoes = entry_anotacoes.get("1.0", tk.END).strip()
            adicionar_entrada(roteiro, materia, anotacoes, data_inicio, data_fim)
            lbl_status.config(text=f"Estudo encerrado em: {data_fim.strftime('%Y-%m-%d %H:%M:%S')}")
            data_inicio = None
        else:
            messagebox.showwarning("Aviso", "O estudo não foi iniciado.")
    
    def salvar_e_sair():
        salvar_roteiro_txt(roteiro)
        root.destroy()

    root = tk.Tk()
    root.title("Roteiro de Estudos")

    tk.Label(root, text="Matéria/Assunto:").grid(row=0, column=0, padx=10, pady=5)
    entry_materia = tk.Entry(root)
    entry_materia.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Anotações:").grid(row=1, column=0, padx=10, pady=5)
    entry_anotacoes = tk.Text(root, height=10, width=40)
    entry_anotacoes.grid(row=1, column=1, padx=10, pady=5)

    btn_iniciar = tk.Button(root, text="Iniciar Estudo", command=iniciar_estudo)
    btn_iniciar.grid(row=2, column=0, padx=10, pady=5)

    btn_pausar = tk.Button(root, text="Pausar Estudo", command=pausar_estudo)
    btn_pausar.grid(row=2, column=1, padx=10, pady=5)

    btn_encerrar = tk.Button(root, text="Encerrar Estudo", command=encerrar_estudo)
    btn_encerrar.grid(row=3, column=0, padx=10, pady=5)

    btn_salvar = tk.Button(root, text="Salvar e Sair", command=salvar_e_sair)
    btn_salvar.grid(row=3, column=1, padx=10, pady=5)

    lbl_status = tk.Label(root, text="Status: Aguardando início do estudo...")
    lbl_status.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
