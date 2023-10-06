import itertools
import csv

def brute_force(actions, budget):
    best_profit = 0
    best_combination = []

    # Générer toutes les combinaisons possibles d'actions
    for i in range(1, len(actions) + 1):
            combinations = itertools.combinations(actions, i)
            # Parcourir chaque combinaison
            for combination in combinations:
                total_cost = sum(action[1] for action in combination if action[1] > 0 or action[2] > 0)

                # Vérifier si le coût total est inférieur ou égal au budget
                if total_cost <= budget:
                    total_profit = sum(action[1] * action[2] for action in combination if action[1] > 0 or action[2] > 0)
                    # Vérifier si le profit total est supérieur au meilleur profit actuel
                    if total_profit > best_profit: 
                        best_profit = total_profit
                        best_combination = combination
                        cost = total_cost
                        print(best_profit)
    with open('combinations.txt', 'a') as f:
                f.write(" Meilleures combinations : "+str(best_combination)+" \n Meilleur profit : "+str(best_profit)+ "\n Cost :"+str(cost))
    return best_combination, best_profit, cost

def optimised(actions, budget):
    actions = [(action, cost, profit, (profit * 100) / cost) for action, cost, profit in actions if cost <= budget and cost > 0 and profit > 0]
    sorted_actions = sorted(actions, key=lambda x :x[3], reverse=True)
    cost = 0
    profit = 0
    buyed = []
    for action in sorted_actions:
        if cost + action[1] <= budget:
            cost += action[1]
            profit += action[3]
            buyed.append((action))
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


actions = [(action, cost, profit, (profit * 100) / cost) for action, cost, profit in actions if  cost > 0 and profit > 0]

