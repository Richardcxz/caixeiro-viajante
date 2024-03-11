import numpy as np
import random as rd
import tkinter as tk

def GerarProblema(n, min, max):
    matz = np.random.randint(min, max, size=(n, n))
    np.fill_diagonal(matz, 0)
    return matz

def SolucaoInicial(n):
    return rd.sample(range(n), n)

def Avalia(sol, matz):
    v = 0
    n = len(matz)

    for i in range(n - 1):
        v += matz[sol[i]][sol[i + 1]]

    v += matz[sol[n - 1]][sol[0]]

    return v

def GerarProblemaInterface():
    n = int(entry_cidades.get())
    min = 15
    max = 60

    global matz
    matz = GerarProblema(n, min, max)
    label_matriz.config(text="Matriz de custo:\n" + str(matz))

def MostrarSolucaoInicial():
    n = int(entry_cidades.get())
    sol = SolucaoInicial(n)
    v = Avalia(sol, matz)
    label_solucao_inicial.config(text=f"Solução inicial: {sol}\nValor da solução inicial: {v}")

# Interface
root = tk.Tk()
root.title("Problema do Caixeiro Viajante")

frame = tk.Frame(root)
frame.pack(expand=True, padx=10, pady=10)

label_cidades = tk.Label(frame, text="Número de cidades até o destino:")
label_cidades.grid(row=0, column=0, padx=5, pady=5)

entry_cidades = tk.Entry(frame)
entry_cidades.grid(row=0, column=1, padx=5, pady=5)

button_gerar_problema = tk.Button(frame, text="Gerar Problema", command=GerarProblemaInterface)
button_gerar_problema.grid(row=0, column=2, padx=5, pady=5)

label_matriz = tk.Label(frame, text="Matriz de custo:")
label_matriz.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

button_mostrar_solucao = tk.Button(frame, text="Mostrar Solução Inicial", command=MostrarSolucaoInicial)
button_mostrar_solucao.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

label_solucao_inicial = tk.Label(frame, text="")
label_solucao_inicial.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Configuração do sistema de gerenciamento de geometria
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure((0, 1, 2), weight=1)

root.mainloop()
