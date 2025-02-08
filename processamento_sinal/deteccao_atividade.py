import numpy as np

def detectar_atividade(sinal_emg, limiar=0.1):
    atividade = np.where(sinal_emg > limiar, 1, 0)
    return atividade
