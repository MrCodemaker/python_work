alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

print(alien_1)

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'red'
print("The alien is " + alien_0['color'] + ".")
