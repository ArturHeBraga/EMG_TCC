from scipy.signal import butter, lfilter
import numpy as np

def filtro_passa_faixa(baixa, alta, fs, ordem=4):
    nyquist = 0.5 * fs
    baixa = baixa / nyquist
    alta = alta / nyquist
    b, a = butter(ordem, [baixa, alta], btype='band')
    return b, a

def aplicar_filtro_passa_faixa(dados, baixa=20, alta=450, fs=1000):
    b, a = filtro_passa_faixa(baixa, alta, fs)
    return lfilter(b, a, dados)

def aplicar_filtro_notch(dados, freq=60, fs=1000, Q=30):
    from scipy.signal import iirnotch
    b, a = iirnotch(freq / (0.5 * fs), Q)
    return lfilter(b, a, dados)

def aplicar_filtros(dados_emg):
    sinal_filtrado = aplicar_filtro_passa_faixa(dados_emg)
    sinal_filtrado = aplicar_filtro_notch(sinal_filtrado)
    sinal_retificado = np.abs(sinal_filtrado)
    sinal_suavizado = np.convolve(sinal_retificado, np.ones(50) / 50, mode='same')
    return sinal_suavizado
