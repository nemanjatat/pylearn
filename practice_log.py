available_movies = ["THE LAST SAMURAI", "300", "KNIVES OUT"]

while True:
    print("Enter movie you want to watch:", end=" ")
    user_movie_input = input()

    if available_movies.__contains__(user_movie_input.upper()):
        print("That movie is available!")
    else:
        print("We don't have that movie!")

    print("Would you like to check for another movie? (Y/N)")
    user_another_movie_answer = input()

    if user_another_movie_answer.upper() == "Y":
        pass
    else:
        break