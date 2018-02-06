print("Pastrami is no more!")

sandwich_orders = ['bocadillo', 'detente', 'crock-madam', 'baths']
finished_sandwiches = []

sandwich_orders.insert(1, 'pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.insert(3, 'pastrami')

while sandwich_orders:
    ready_sandwiche = sandwich_orders.pop()

    print("Preparation: " + ready_sandwiche.title())
    finished_sandwiches.append(ready_sandwiche)

print("\nI made your " + ready_sandwiche + " sandwich")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

while 'pastrami' in finished_sandwiche:
    finished_sandwiche.remove('pastrami')

print(finished_sandwiche)
