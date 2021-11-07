import csv
import matplotlib.pyplot

beta = 0
gamma = 0
S = []
I = []
R = []
N = 30

with open("test-sir-data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    beta = float(data[0][1])
    gamma = float(data[0][3])
    for row in data[2:len(data)]:
        S.append(float(row[1]))
        I.append(float(row[2]))
        R.append(float(row[3]))

with open("test-sir-output.csv", "w") as f:
    writer = csv.writer(f)
    fields = ["Date", "S", "I", "R"]
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerow({'Date': 0, 'S': S[0], 'I': I[0], 'R': R[0]})
    for i in range(1, N):
        S.append(S[-1] - beta * I[-1] * S[-1])
        I.append(I[-1] + beta * I[-1] * S[-1] - gamma * I[-1])
        R.append(R[-1] + gamma * I[-1])
        writer.writerow({'Date': i, 'S': S[-1], 'I': I[-1], 'R': R[-1]})

fig, sir_chart = matplotlib.pyplot.subplots()
sir_chart.plot(S, label='S')
sir_chart.plot(I, label='I')
sir_chart.plot(R, label='R')
matplotlib.pyplot.show()
