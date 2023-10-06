import csv

def optimised(actions, budget):
    sorted_actions = sorted(actions, key=lambda x :x[3], reverse=True)
    cost = 0
    profit = 0
    buyed = []
    for action in sorted_actions:
        if cost + action[1] <= budget:
            cost += action[1]
            profit += action[3]
            buyed.append((action))
    with open('optimised.txt', 'a') as f:
        f.write(" Meilleures combinations : "+str(buyed)+" \n Meilleur profit : "+str(profit)+ "\n Cost :"+str(cost))
    return cost, profit, buyed



actions = []

# Citirea primului fisier CSV
with open('data1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    next(reader1)  # Sari peste header daca exista
    for row in reader1:
        action = (row[0], float(row[1]), float(row[2]))
        actions.append(action)

# Citirea celui de-al doilea fisier CSV
with open('data2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    next(reader2)  # Sari peste header daca exista
    for row in reader2:
        action = (row[0], float(row[1]), float(row[2]))
        actions.append(action)

actions = [(action, cost, profit, (profit / 100) * cost) for action, cost, profit in actions if  cost > 0 and profit > 0]


optimised(actions,500)