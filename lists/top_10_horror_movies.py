top_10_horror_movies = []

top_10_horror_movies.append('the silence of the lambs')
top_10_horror_movies.append('psycho')
top_10_horror_movies.append('the others')
top_10_horror_movies.append('sleepy hollow')
top_10_horror_movies.append('aliens')
top_10_horror_movies.append('alien')
top_10_horror_movies.append('interview with the vampire: the vampire Chronicles')
top_10_horror_movies.append('i am legend')
top_10_horror_movies.append('saw')
top_10_horror_movies.append('from dusk till dawn')

print("\nTop-10 horror movies:")

print(top_10_horror_movies)

print(len(top_10_horror_movies))

top_10_horror_movies.sort()
print(top_10_horror_movies)

movies = top_10_horror_movies

movies.sort(reverse = True)
print(movies)

sorted(movies)
print(movies)

sorted(movies, reverse = True)
print(movies)

popped_movies = movies.pop(3)
print(popped_movies.title() + " has been delete!")

print(movies)

movies.insert(3, 'misery')
print(movies[3].title() + " has been insert on 3-th position!")
print(movies)




