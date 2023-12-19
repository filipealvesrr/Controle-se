import csv
import matplotlib.pyplot as plt

data = {'RPM': []}
with open('dados.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data['RPM'].append(float(row['RPM']))

plt.subplot(1, 1, 1)
plt.plot(data['RPM'], label='Valores RPM', color='orange', marker='o')
plt.title('Valores de RPM ao longo do tempo')
plt.xlabel('Amostras')
plt.ylabel('Valores RPM')
plt.legend()

plt.tight_layout()
plt.show()
