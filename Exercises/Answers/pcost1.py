
def portfolio_cost(file_name):

    cost = 0.0

    with open(file_name, "r") as f:
        
            for line in f:
                s = line.split()
                try:
                    shares = int(s[1])
                    price = float(s[2])
                    cost = cost + shares * price
                except ValueError as e:
                    print("Couldn't Parse:", repr(line))
                    print("Reason:", e)
    return cost

