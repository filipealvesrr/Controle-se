import csv
import matplotlib.pyplot as plt

data = {'Tempo': [], 'RPM': []}
amostra_atual = 0

with open('dadosTempo.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data['Tempo'].append(amostra_atual)
        data['RPM'].append(float(row['RPM']))
        amostra_atual += 1

plt.plot(data['Tempo'], data['RPM'], label='Valores RPM', color='orange', marker='o')
plt.title('Valores de RPM ao longo de 5 minutos')
plt.xlabel('Tempo (Segundos)')
plt.ylabel('Valores RPM')
plt.legend()

plt.tight_layout()
plt.show()
