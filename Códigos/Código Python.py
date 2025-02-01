# Bibliotecas Essenciais para o código
import serial
# Bibliotecas Opcionais
from time import sleep
from pynput.keyboard import Controller

# Conexão do Serial do Arduino com o Python, a porta COM3 poderá mudar de casa para caso
arduino = serial.Serial('COM3',9600)
keyboard = Controller()

print("Aguardando comandos do Arduino...")

# Looping para manter o Python esperando os comandos do Arduino
while True:
	if arduino.in_waiting > 0:

		# Função para Ler os Inputs do Serial e transformar em Variável 
		button_index = arduino.readline().decode().strip()
		
		# Configurações para cada botão. Altere a vontade a partir de suas necessidades
		match button_index:
			case 0:
				# Exemplo digitando "Hello World" em um campo de texto
				print("Botão 1 pressionado!")
				keyboard.type("Hello, World!\n")
			case 1:
				# Exemplo pressionando a tecla "A"
				keyboard.press('a')
				keyboard.press('a')
				keyboard.release('a')
			case 2:
				# Exemplo abrindo o navegador (Com ajuda de uma biblioteca)
				print("Abrindo navegador...")
				import os
				os.system("start chrome")
			case 3:
				# Exemplo digitando "Texto do Botão 4" em um campo de texto
				print("Botão 4 pressionado!")
				keyboard.type("Texto do Botão 4\n")