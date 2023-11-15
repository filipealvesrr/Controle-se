import serial
import csv
import time


ser = serial.Serial('COM4', 9600)  
totalAmostras = 30

with open('dados.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['PWM', 'RPM', 'Cont']) 

    try:
        contAmostras = 0
        while contAmostras < totalAmostras:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                values = line.split(',')
                csv_writer.writerow(values)
                contAmostras += 1

    except KeyboardInterrupt:
        ser.close()
        print("Conexão encerrada.")
