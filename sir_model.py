import csv
import matplotlib.pyplot


## Prepare SIR model parameters

# Infectious rate
beta = 0.5

# Recovery rate
gamma = 1/15

# Susceptible - Infectious - Recovered
S = []
I = []
R = []

# Days to forecast
N = 365

with open("test-sir-data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data[1:2]:
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
        curr_S = S[-1]
        curr_I = I[-1]
        curr_R = R[-1]
        S.append(curr_S - beta * curr_I * curr_S)
        I.append(curr_I + beta * curr_I * curr_S - gamma * curr_I)
        R.append(curr_R + gamma * curr_I)
        writer.writerow({'Date': i, 'S': S[-1], 'I': I[-1], 'R': R[-1]})

fig, sir_chart = matplotlib.pyplot.subplots()
sir_chart.plot(S, label='S')
sir_chart.plot(I, label='I')
sir_chart.plot(R, label='R')
matplotlib.pyplot.show()
