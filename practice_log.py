class Movie:
    def __init__(self, name, genre, year):
        self.name = name
        self.genre = genre
        self.year = year

    def display_info(self):
        print(f"Movie name:\t\t{self.name}\nMovie genre:\t{self.genre}\nMovie year:\t\t{self.year}")

print("Movie name: ")
name = input()

print("Movie genre: ")
genre = input()

print("Movie release year: ")
year = input()

movie = Movie(name, genre, year)

movie.display_info()