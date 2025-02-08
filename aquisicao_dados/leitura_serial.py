import serial
import threading

class LeitorSerial:
    def __init__(self, porta='COM3', baudrate=9600, callback=None):
        self.serial = serial.Serial(porta, baudrate)
        self.callback = callback
        self.rodando = False

    def iniciar(self):
        self.rodando = True
        threading.Thread(target=self.ler_dados, daemon=True).start()

    def parar(self):
        self.rodando = False
        self.serial.close()

    def ler_dados(self):
        while self.rodando:
            if self.serial.in_waiting:
                dado_bruto = self.serial.readline().decode().strip()
                try:
                    valor_emg = float(dado_bruto)
                    if self.callback:
                        self.callback(valor_emg)
                except ValueError:
                    continue
