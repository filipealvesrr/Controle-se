import csv
import matplotlib.pyplot as plt

data = {'PWM': []}
with open('dadosPWM.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data['PWM'].append(float(row['PWM']))

plt.subplot(1, 1, 1)
plt.plot(data['PWM'], label='Valores PWM', color='orange', marker='o')
plt.title('Valores de PWM por amostras')
plt.xlabel('Amostras')
plt.ylabel('Valores PWM')
plt.legend()

plt.tight_layout()
plt.show()
