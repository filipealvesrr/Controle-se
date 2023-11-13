import serial
import matplotlib.pyplot as plt
from drawnow import drawnow
import re

ser = serial.Serial('COM4', 9600)
pwm_values = []
rpm_values = []

def plotarGrafico():
    plt.subplot(2, 1, 1)
    plt.plot(pwm_values, label='Valores PWM')
    plt.title('Valores de PWM e RPM ao longo do tempo')
    plt.xlabel('Amostra')
    plt.ylabel('Valor PWM')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(rpm_values, label='Valores RPM', color='orange')
    plt.xlabel('Amostras')
    plt.ylabel('Valor RPM')
    plt.legend()

def atualizarGrafico():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()

            pwm_match = re.search(r'PWM=(\d+)', line)
            rpm_match = re.search(r'RPM=(\d+)', line)

            if pwm_match:
                pwm_value = int(pwm_match.group(1))
                rpm_value = int(rpm_match.group(1))

                pwm_values.append(pwm_value)
                rpm_values.append(rpm_value)

            drawnow(plotarGrafico)

try:
    atualizarGrafico()

except KeyboardInterrupt:
    ser.close()
    print("Conexão encerrada.")