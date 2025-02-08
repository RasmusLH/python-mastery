cost = 0.0

with open("Data\portfolio.dat", "r") as f:
    for line in f:
        s = line.split()
        shares = int(s[1])
        price = float(s[2])
        cost = cost + shares * price

print(cost)