import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from aquisicao_dados.leitura_serial import LeitorSerial
from processamento_sinal.filtros import aplicar_filtros
from processamento_sinal.deteccao_atividade import detectar_atividade

class AplicativoEMG:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Analisador de Sinais EMG")

        # Configuração do gráfico
        self.figura, self.eixo = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.janela)
        self.canvas.get_tk_widget().pack()

        # Botões de controle
        frame_controles = ttk.Frame(self.janela)
        frame_controles.pack(pady=5)

        self.botao_iniciar = ttk.Button(frame_controles, text="Iniciar", command=self.iniciar_aquisicao)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_parar = ttk.Button(frame_controles, text="Parar", command=self.parar_aquisicao)
        self.botao_parar.grid(row=0, column=1, padx=5)

        # Inicialização da leitura serial
        self.leitor = LeitorSerial(callback=self.atualizar_grafico)

    def iniciar_aquisicao(self):
        self.leitor.iniciar()

    def parar_aquisicao(self):
        self.leitor.parar()

    def atualizar_grafico(self, dados_emg):
        sinal_filtrado = aplicar_filtros(dados_emg)
        atividade = detectar_atividade(sinal_filtrado)

        self.eixo.clear()
        self.eixo.plot(sinal_filtrado, label="Sinal EMG Filtrado")
        self.eixo.plot(atividade * max(sinal_filtrado), 'r--', label="Atividade Detectada")
        self.eixo.legend()
        self.canvas.draw()

    def executar(self):
        self.janela.mainloop()
