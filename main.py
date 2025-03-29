import serial
import numpy as np
import time

# Configuração da porta serial
porta_serial = 'COM5'  
taxa_baud = 115200
ser = serial.Serial(porta_serial, taxa_baud)

# Parâmetros
SAMPLE_COUNT = 100  
fs = 500            
fator_k = 3         


dados_emg = []

# Função para calcular o threshold fixo com base nas amostras iniciais
def calculate_threshold(dados):
    media = np.mean(dados)
    desvio_padrao = np.std(dados)
    return media + fator_k * desvio_padrao  

# Coleta inicial para definir o threshold
initial_data = []
for _ in range(SAMPLE_COUNT):
    linha_serial = ser.readline().decode('utf-8').strip()
    if linha_serial:
        try:
            valor = int(linha_serial)
            initial_data.append(valor)
        except ValueError:
            pass

threshold = calculate_threshold(initial_data)
print(f"Threshold definido: {threshold:.2f}")

# Loop principal para leitura do EMG
while True:
    linha_serial = ser.readline().decode('utf-8').strip()
    if linha_serial:
        try:
            valor = int(linha_serial)
            dados_emg.append(valor)

            
            if len(dados_emg) > SAMPLE_COUNT:
                dados_emg.pop(0)

            print(f"Valor EMG Atual: {valor}")

            # Detecta picos
            if valor > threshold:
                print("Pico detectado! Enviando comando para o Arduino.")
                # Comandos para mover o servo
                ser.write(b'1')  
                time.sleep(2)
                ser.write(b'0')
        except ValueError:
            pass

    time.sleep(0.01) 
