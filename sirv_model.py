import csv
import matplotlib.pyplot


## Prepare SIR model parameters

# Infectious rate
beta = 0.5

# Recovery rate
gamma = 1/15

# Vaccine effects
v_effect = [0.5, 0.9]

# Susceptible - Infectious - Recovered
S = []
I = []
R = []
V1 = []
V2 = []

# Days to forecast
N = 90

with open("test-sir-data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    S.append(float(data[1][1]))
    I.append(float(data[1][2]))
    R.append(float(data[1][3]))
    for row in data[1:len(data)]:
        V1.append(float(row[4]))
        V2.append(float(row[5]))

with open("test-sirv-output.csv", "w") as f:
    writer = csv.writer(f)
    fields = ["Date", "S", "I", "R"]
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerow({'Date': 0, 'S': S[0], 'I': I[0], 'R': R[0]})
    for i in range(1, N):
        curr_S = S[-1]
        curr_I = I[-1]
        curr_R = R[-1]
        curr_V1 = V1[i - 1]
        curr_V2 = V2[i - 1]

        S.append(curr_S - beta * curr_I * (curr_S - v_effect[0] * curr_V1 - v_effect[1] * curr_V2))
        I.append(curr_I + beta * curr_I * (curr_S - v_effect[0] * curr_V1 - v_effect[1] * curr_V2) - gamma * curr_I)
        R.append(curr_R + gamma * curr_I)
        writer.writerow({'Date': i, 'S': S[-1], 'I': I[-1], 'R': R[-1]})

fig, sir_chart = matplotlib.pyplot.subplots()
sir_chart.plot(S, label='S')
sir_chart.plot(I, label='I')
sir_chart.plot(R, label='R')
matplotlib.pyplot.show()
