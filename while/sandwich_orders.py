sandwich_orders = ['bocadillo', 'detente', 'crock-madam', 'baths']
finished_sandwiches = []

while sandwich_orders:
    ready_sandwiche = sandwich_orders.pop()

    print("Preparation: " + ready_sandwiche.title())
    finished_sandwiches.append(ready_sandwiche)

print("\nI made your " + ready_sandwiche + " sandwich")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
