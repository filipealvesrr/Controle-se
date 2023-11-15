import csv
import matplotlib.pyplot as plt

data = {'PWM': [], 'RPM': []}
with open('dados.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data['PWM'].append(int(row['PWM']))
        data['RPM'].append(int(row['RPM']))

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(data['PWM'], label='Valores PWM', marker='o')
plt.title('Valores de PWM ao longo do tempo')
plt.xlabel('Amostras')
plt.ylabel('Valores PWM')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(data['RPM'], label='Valores RPM', color='orange', marker='o')
plt.title('Valores de RPM ao longo do tempo')
plt.xlabel('Amostras')
plt.ylabel('Valores RPM')
plt.legend()

plt.tight_layout()
plt.show()
