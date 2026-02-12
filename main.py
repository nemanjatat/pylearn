# typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

movie_name = "Crime 101"
release_year = 2026
score = 3.3
in_cinemas = True

print(f"Movie name's original type: {type(movie_name)}")
movie_name = bool(movie_name)
print(f"Movie name's altered type: {type(movie_name)}")

print(f"Release year's original type: {type(release_year)}")
release_year = float(release_year)
print(f"Release year's altered type: {type(release_year)}")

print(f"Score's original type: {type(score)}")
score = int(score)
print(f"Score's altered type: {type(score)}")

print(f"in_cinema's origianl type: {type(in_cinemas)}")
in_cinemas = str(in_cinemas)
print(f"in_cinema's altered type: {type(in_cinemas)}")

print("Conclusion\n============")
print(f"Movie Name: {movie_name}")
print(f"Release Year: {release_year}")
print(f"Score: {score}")
print(f"In Cinemas: {in_cinemas}")