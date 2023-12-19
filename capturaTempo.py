import serial
import csv
import time

ser = serial.Serial('COM4', 9600)  
tempo_maximo_segundos = 300  # Defina o tempo máximo de execução em segundos

with open('dadosTempo.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Tempo', 'RPM']) 

    tempo_inicio = time.time()

    try:
        amostra_atual = 0
        while (time.time() - tempo_inicio) < tempo_maximo_segundos:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                tempo_atual = time.time() - tempo_inicio
                values = [tempo_atual, line]
                csv_writer.writerow(values)
                amostra_atual += 1
                
    except KeyboardInterrupt:
        pass  # Permite interromper o programa usando Ctrl+C

    finally:
        ser.close()
        print("Conexão encerrada.")
